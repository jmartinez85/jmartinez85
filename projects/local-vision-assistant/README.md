![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Local Vision Assistant

Multimodal AI prototypes

## Objective

Ask questions in natural language about webcam images and process those images locally.

## Implementation

Users choose which webcam frame to send to the model. One version uses Gradio and GGUF models through llama.cpp. Another runs Qwen2-VL through Transformers.

## Technologies

Python, OpenCV, Gradio, llama.cpp, Transformers.

## Run the demo

```sh
python app.py examples/demo-image.jpg --dry-run
python app.py examples/demo-image.jpg "How many shapes are present?"
```

The dry run reports the model and input size. With a [local Ollama vision model](docs/model-setup.md), the second command sends the synthetic image to the model and prints its answer.

[Back to the portfolio](../../README.md)
