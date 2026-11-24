import { stepsFor } from "./warehouse-comms.js";

const elements = Object.fromEntries(
  ["store", "retrieve", "next", "status", "scene", "messages"].map(id => [id, document.getElementById(id)])
);
const ctx = elements.scene.getContext("2d");
const coordinates = { infeed: [90, 160], transit: [340, 110], rack: [590, 62] };
let position = "infeed";
let steps = [];
let cursor = 0;

function render() {
  elements.store.disabled = position !== "infeed" || cursor < steps.length;
  elements.retrieve.disabled = position !== "rack" || cursor < steps.length;
  elements.next.disabled = cursor >= steps.length;
  ctx.clearRect(0, 0, 720, 220);
  ctx.strokeStyle = "#6789a2";
  ctx.strokeRect(55, 115, 120, 80);
  ctx.strokeRect(550, 22, 130, 165);
  ctx.fillStyle = "#e9f2fa";
  ctx.font = "16px system-ui";
  ctx.fillText("Infeed / outfeed", 55, 212);
  ctx.fillText("Storage rack", 552, 212);
  const [x, y] = coordinates[position];
  ctx.fillStyle = "#54d7ff";
  ctx.fillRect(x, y, 55, 24);
}

function advance() {
  const [actor, message, destination] = steps[cursor++];
  position = destination;
  elements.status.value = message;
  elements.messages.textContent += actor + " — " + message + "\n";
  render();
}

function start(command) {
  steps = stepsFor(command);
  cursor = 0;
  elements.messages.textContent = "";
  advance();
}

elements.store.addEventListener("click", () => start("store"));
elements.retrieve.addEventListener("click", () => start("retrieve"));
elements.next.addEventListener("click", advance);
elements.status.value = "Pallet ready at the infeed.";
render();
