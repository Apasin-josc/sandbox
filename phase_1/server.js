import http from "node:http";

const server = http.createServer((req, res) => {

    if (req.method === "GET" && req.url === "/"){
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify("home page"));
    }
  
    if (req.method === "GET" && req.url === "/habits") {
    const habits = [
      { id: 1, name: "read", done: true },
      { id: 2, name: "run", done: false },
    ];
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(habits));
  } else {
    res.writeHead(404, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "Not found" }));
  }
});


server.listen(3000, () => {
    console.log(`server running on http://localhost:3000`);
});