const selector = document.getElementById("trajectory");
const next = document.getElementById("next");
const reset = document.getElementById("reset");
const status = document.getElementById("status");
const ctx = document.getElementById("scene").getContext("2d");
const colors = ["#54d7ff", "#ffc77a"];

async function run() {
  const response = await fetch("../examples/trajectory-demo.csv");
  if (!response.ok) throw new Error("The trajectory file could not be loaded.");
  const rows = (await response.text()).trim().split(/\r?\n/).slice(1).map(line => {
    const [path, robot, step, x, y] = line.split(",");
    return { path, robot: Number(robot), step: Number(step), x: Number(x), y: Number(y) };
  });
  let current = 0;
  function render() {
    const waypoints = rows.filter(row => row.path === selector.value);
    const last = Math.max(...waypoints.map(row => row.step));
    ctx.clearRect(0, 0, 720, 290);
    ctx.strokeStyle = "#6789a2";
    ctx.strokeRect(313, 98, 94, 100);
    for (const robot of [1, 2]) {
      const track = waypoints.filter(row => row.robot === robot);
      ctx.strokeStyle = ctx.fillStyle = colors[robot - 1];
      ctx.beginPath();
      ctx.moveTo(track[0].x, track[0].y);
      for (const point of track.slice(1)) ctx.lineTo(point.x, point.y);
      ctx.stroke();
      const point = track.find(row => row.step === current);
      ctx.beginPath();
      ctx.arc(point.x, point.y, 8, 0, 2 * Math.PI);
      ctx.fill();
    }
    status.value = selector.value + " — waypoint " + (current + 1) + " of " + (last + 1);
    next.disabled = current === last;
    reset.disabled = current === 0;
  }
  next.addEventListener("click", () => { current += 1; render(); });
  for (const [element, event] of [[selector, "change"], [reset, "click"]]) {
    element.addEventListener(event, () => { current = 0; render(); });
  }
  render();
}

run().catch(error => { status.value = error.message; });
