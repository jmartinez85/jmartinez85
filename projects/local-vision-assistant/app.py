"""Ask a locally hosted Ollama vision model about an image."""

import argparse
import base64
import json
import os
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("question", nargs="?", default="What colors and shapes are visible?")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    image = args.image.read_bytes()
    model = os.environ.get("OLLAMA_VISION_MODEL", "llama3.2-vision")
    if args.dry_run:
        print(json.dumps({"model": model, "image_bytes": len(image), "question": args.question}))
        return
    url = os.environ.get("OLLAMA_URL", "http://localhost:11434").rstrip("/")
    payload = json.dumps({
        "model": model,
        "prompt": args.question,
        "images": [base64.b64encode(image).decode("ascii")],
        "stream": False,
    }).encode("utf-8")
    request = Request(f"{url}/api/generate", data=payload, headers={"Content-Type": "application/json"})
    try:
        with urlopen(request, timeout=90) as response:
            result = json.load(response)
        print(result["response"])
    except (URLError, OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Vision request failed: {error}\n")


if __name__ == "__main__":
    main()
