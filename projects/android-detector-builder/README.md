![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Android Detector Builder

Build tool

## Objective

Package custom Android detectors from pretrained models in NCNN format.

## Implementation

Each model has a manifest that specifies its version, classes, and files. The builder validates the inputs, copies an existing Android template, replaces the model and labels, and builds the APK with Gradle.

## Technologies

Python, Android, Gradle, NCNN.

## Run the demo

```sh
python scripts/build_detector.py models/my-detector/manifest.json --validate-only
python scripts/build_detector.py models/my-detector/manifest.json --template /path/to/compatible-template
```

Copy [the example manifest](models/_template/manifest.json.example) and supply your own compatible model assets. Validation reports the detector version and class count. With the matching template and Android toolchain, the build stages the model and labels and writes `builds/detector-debug.apk`. See [build inputs](docs/android-build.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

[Back to the portfolio](../../README.md)
