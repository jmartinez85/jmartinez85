![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Hybrid Municipal Chatbot

Web application and API

## Objective

Answer common questions using information configured for each chatbot.

## Implementation

The orchestrator combines rule-based responses, FAQ retrieval, and an adapter for a local language model. A web portal lets the team configure parameters and suggested prompts for each chatbot.

## Technologies

Python, FastAPI, Pydantic, JavaScript.

## Run the demo

```sh
python -m pip install -r requirements.txt
python -m uvicorn services.api.main:app --host 127.0.0.1 --port 8000
```

Open [the chatbot](http://localhost:8000/) and ask about opening hours. The demo uses a fictional FAQ and shows whether a rule, retrieval, or the fallback handled each question. Run `python -m unittest discover -s tests/unit` to verify routing.

[Back to the portfolio](../../README.md)
