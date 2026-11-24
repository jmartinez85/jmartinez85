const output = document.querySelector("output");
const canvas = document.querySelector("canvas");
const view = canvas.getContext("2d");

async function update(action) {
  try {
    const route = action ? "/api/camera?action=" + encodeURIComponent(action) : "/api/camera";
    const response = await fetch(route, { method: action ? "POST" : "GET" });
    const state = await response.json();
    if (!response.ok) throw new Error(state.error);
    const { pan, tilt, zoom } = state;
    output.value = `Pan ${pan}° · Tilt ${tilt}° · Zoom ${zoom}×`;
    view.fillStyle = "#1b3349";
    view.fillRect(0, 0, canvas.width, canvas.height);
    view.fillStyle = "#67deff";
    view.beginPath();
    view.arc(320 - pan * 3, 110 + tilt * 1.8, 10 * zoom, 0, Math.PI * 2);
    view.fill();
  } catch (error) {
    output.value = error.message;
  }
}

document.getElementById("controls").addEventListener("click", event => {
  const action = event.target.dataset.action;
  if (action) update(action);
});
update();
