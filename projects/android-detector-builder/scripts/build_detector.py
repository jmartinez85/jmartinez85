"""Package an NCNN model using the matching Android detector template."""

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

from coco_classes import COCO_EN

ANDROID_MAIN = Path("app/src/main")


def load_model(manifest_path):
    manifest = json.loads(manifest_path.read_text())
    if not isinstance(manifest, dict):
        raise ValueError("Expected a JSON object in the manifest.")
    assets = []
    for key in ("param", "bin"):
        name = manifest[key]
        if not isinstance(name, str) or name in {"", ".", ".."} or Path(name).name != name:
            raise ValueError(f"Expected a filename for {key}.")
        asset = manifest_path.parent / name
        if not asset.is_file() or asset.stat().st_size == 0:
            raise ValueError(f"Missing or empty model asset: {asset}")
        assets.append(asset)
    with assets[0].open(encoding="utf-8") as param:
        if param.readline().strip() != "7767517":
            raise ValueError("The .param file has an unexpected NCNN header.")
    labels = manifest.get("classes", COCO_EN if manifest.get("classes_from") == "coco" else None)
    if not isinstance(labels, (list, tuple)) or not labels or any(
        not isinstance(label, str) or not label for label in labels
    ):
        raise ValueError("Supply class labels or set classes_from to coco.")
    if len(labels) != manifest.get("num_classes", len(labels)):
        raise ValueError("Class count does not match the supplied labels.")
    if manifest.get("input_size") not in {320, 480, 640}:
        raise ValueError("The template supports input sizes 320, 480 and 640.")
    code = manifest.get("version_code")
    if type(code) is not int or not 0 < code <= 2_100_000_000:
        raise ValueError("Specify a valid positive integer version_code.")
    for key in ("display_name", "version"):
        if not isinstance(manifest.get(key), str) or not manifest[key]:
            raise ValueError(f"Specify a nonempty {key}.")
    return manifest, assets, labels


def substitute(text, pattern, replacement, field):
    updated, count = re.subn(pattern, lambda match: replacement(match), text, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected {field} in the matching Android template.")
    return updated


def patch_template(workspace, manifest, assets, labels):
    main = workspace / ANDROID_MAIN
    resources = main / "res/values/strings.xml"
    strings = substitute(
        resources.read_text(), r'(<string name="app_name">).*?(</string>)',
        lambda match: match[1] + escape(manifest["display_name"]) + match[2], "app_name"
    )
    strings = substitute(
        strings, r'(<string-array name="model_array">).*?(</string-array>)',
        lambda match: match[1] + f'<item>n-{manifest["input_size"]}</item>' + match[2], "model_array"
    )
    resources.write_text(strings)

    path = main / "AndroidManifest.xml"
    xml = path.read_text()
    for field, value in [("versionCode", manifest["version_code"]), ("versionName", manifest["version"])]:
        escaped = escape(str(value), {'"': "&quot;"})
        xml = substitute(xml, rf'android:{field}="[^"]*"', lambda _: f'android:{field}="{escaped}"', field)
    path.write_text(xml)

    label_path = main / "jni/yolov8ncnn.cpp"
    cpp = label_path.read_text()
    padded = list(labels) + [f"class_{index}" for index in range(len(labels), 80)]
    items = ",\n    ".join(json.dumps(label, ensure_ascii=False) for label in padded)
    for language in ("en", "es", "it"):
        pattern = rf"(static const char\* const coco_names_{language}\[\] = \{{).*?(\}};)"
        cpp = substitute(cpp, pattern, lambda match: match[1] + "\n    " + items + "\n" + match[2], language)
    label_path.write_text(cpp)

    target = main / "assets"
    target.mkdir(parents=True, exist_ok=True)
    for asset, name in zip(assets, ("yolov8n.ncnn.param", "yolov8n.ncnn.bin")):
        shutil.copyfile(asset, target / name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--template", type=Path, help="Path to the compatible Android template")
    parser.add_argument("--output", type=Path, default=Path("builds/detector-debug.apk"))
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--offline", action="store_true", help="Use cached Gradle dependencies")
    args = parser.parse_args()
    try:
        manifest, assets, labels = load_model(args.manifest)
        print(f"{manifest['display_name']} {manifest['version']}: {len(labels)} classes")
        if args.validate_only:
            return
        template = args.template or os.environ.get("BASE_PROJECT")
        if not template:
            parser.error("Supply --template or set BASE_PROJECT.")
        with tempfile.TemporaryDirectory(prefix="detector-") as directory:
            workspace = Path(directory) / "app"
            shutil.copytree(
                Path(template).expanduser().resolve(), workspace, symlinks=True,
                ignore=shutil.ignore_patterns(".git", "build", ".gradle", ".idea", "local.properties")
            )
            patch_template(workspace, manifest, assets, labels)
            environment = os.environ.copy()
            sdk = environment.get("ANDROID_SDK")
            if sdk:
                environment.setdefault("ANDROID_HOME", sdk)
            command = ["./gradlew", "--offline", "assembleDebug"] if args.offline else ["./gradlew", "assembleDebug"]
            subprocess.run(command, check=True, cwd=workspace, env=environment)
            packages = sorted((workspace / "app/build/outputs/apk/debug").glob("*.apk"))
            if len(packages) != 1:
                raise ValueError(f"Expected one debug APK, found {len(packages)}.")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(packages[0], args.output)
        print(f"Wrote {args.output}")
    except (OSError, KeyError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
