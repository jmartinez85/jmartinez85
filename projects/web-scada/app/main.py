import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .plc_simulator import PLCSimulator

ROOT = Path(__file__).resolve().parents[1]
tags = json.loads((ROOT / "examples/tags.example.json").read_text())
plc = PLCSimulator(tags["line_speed_samples"], tags["line_speed_limit"])
app = FastAPI(title="Simulated SCADA")
app.mount("/static", StaticFiles(directory=ROOT / "static"), name="static")
templates = Jinja2Templates(directory=ROOT / "templates")


@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="dashboard.html")


@app.get("/api/tags")
def read_tags():
    return plc.read()
