import { readFile } from "node:fs/promises";
import { createServer } from "node:http";

import { MockCamera } from "./demo/mock-camera.js";

const camera = new MockCamera();
const pages = new Map([
  ["/", ["./public/index.html", "text/html; charset=utf-8"]],
  ["/main.js", ["./public/main.js", "text/javascript; charset=utf-8"]]
]);

function json(response, status, payload) {
  response.writeHead(status, { "Content-Type": "application/json; charset=utf-8" });
  response.end(JSON.stringify(payload));
}

const server = createServer(async (request, response) => {
  const url = new URL(request.url, "http://localhost");
  try {
    if (request.method === "GET" && pages.has(url.pathname)) {
      const [path, contentType] = pages.get(url.pathname);
      const content = await readFile(new URL(path, import.meta.url));
      response.writeHead(200, { "Content-Type": contentType });
      response.end(content);
    } else if (request.method === "GET" && url.pathname === "/api/camera") {
      json(response, 200, camera.position);
    } else if (request.method === "POST" && url.pathname === "/api/camera") {
      json(response, 200, camera.command(url.searchParams.get("action")));
    } else {
      json(response, 404, { error: "Not found" });
    }
  } catch (error) {
    if (error instanceof RangeError) {
      json(response, 400, { error: error.message });
    } else {
      console.error(error);
      json(response, 500, { error: "The demo could not process the request." });
    }
  }
});

const port = Number(process.env.PORT || 8080);
server.listen(port, "127.0.0.1", () => console.log(`Listening on http://localhost:${port}`));
