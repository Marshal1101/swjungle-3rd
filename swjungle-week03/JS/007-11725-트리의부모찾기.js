// 86	43482265	1	marshal1101	85564	748	node.js 	826	

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const N = +input.shift();
const graph = [];

for (let i = 1; i < N+1; i++) {
    graph[i] = [];
}
for (let i = 0; i < input.length; i++) {
    const [v1, v2] = input[i].split(' ').map(Number);
    graph[v1].push(v2);
    graph[v2].push(v1);
}

const visited = new Array(N+1).fill(false);
const parent = Array.from({ length: N + 1 }, (_, i) => i);
function bfs(v) {
    const queue = [v];
    visited[v] = true;
    let ptr = 0;
    while (queue.length > ptr) {
        const e1 = queue[ptr++];                // shift() 보다 ptr 이동이 빠름
        for (const e2 of graph[e1]) {
            if (visited[e2] === false) {
                visited[e2] = true;
                queue.push(e2);
                parent[e2] = e1;
            }
        }
    }
}

bfs(1);
console.log(parent.slice(2).join('\n'));