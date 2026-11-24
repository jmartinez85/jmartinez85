const area = document.getElementById("area");
const list = document.getElementById("projects");
const count = document.getElementById("count");

async function run() {
  const response = await fetch("../examples/projects.json");
  if (!response.ok) throw new Error("The catalog could not be loaded.");
  const projects = await response.json();
  const categories = new Set(projects.map(project => project.area));
  for (const category of categories) area.add(new Option(category, category));
  function render() {
    const visible = projects.filter(project => !area.value || project.area === area.value);
    list.replaceChildren(...visible.map(project => {
      const item = document.createElement("li");
      const title = document.createElement("strong");
      title.textContent = project.title;
      item.append(title, " — " + project.summary);
      return item;
    }));
    count.value = visible.length + " project(s)";
  }
  area.addEventListener("change", render);
  render();
}

run().catch(error => { count.value = error.message; });
