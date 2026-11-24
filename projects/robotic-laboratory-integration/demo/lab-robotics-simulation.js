const next = document.getElementById("next");
const reset = document.getElementById("reset");
const status = document.getElementById("status");
const stations = document.getElementById("stations");
const details = document.getElementById("event");

async function run() {
  const response = await fetch("../examples/sample-events.json");
  if (!response.ok) throw new Error("The sample events could not be loaded.");
  const events = await response.json();
  let current = 0;
  function render() {
    const event = events[current];
    stations.replaceChildren(...events.map((step, index) => {
      const item = document.createElement("li");
      item.textContent = step.station;
      if (index === current) item.setAttribute("aria-current", "step");
      return item;
    }));
    status.value = event.station + " — " + event.state;
    details.textContent = JSON.stringify(event, null, 2);
    next.disabled = current === events.length - 1;
    reset.disabled = current === 0;
  }
  next.addEventListener("click", () => { current += 1; render(); });
  reset.addEventListener("click", () => { current = 0; render(); });
  render();
}

run().catch(error => { status.value = error.message; });
