import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from services.orchestrator.service import FAQResponder

ROOT = Path(__file__).resolve().parents[2]
responder = FAQResponder(json.loads((ROOT / "knowledge/faqs/demo.json").read_text()))
app = FastAPI(title="Municipal FAQ Demo")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)


@app.get("/")
def frontend():
    return FileResponse(ROOT / "frontend/index.html")


@app.post("/api/chat")
def chat(request: ChatRequest):
    return responder.answer(request.message)
