// 3	43831011	4	marshal1101	9688	116	node.js 	995

let [N, M, ...arr] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');
N = +N;
M = +M;
const graph = Array(N + 1).fill(null).map(ele => []);
const indegree = Array(N + 1).fill(0);
const count = Array(N + 1).fill(0);
// u -> v graph, indegree
arr.forEach((line) => {
    const [u, v, era] = line.split(' ').map(Number);
    graph[u].push([v, era]);
    indegree[v] += 1;
});

const queue = [];
for (let i = 1; i < N + 1; i++) {
    if (!indegree[i]) {
        queue.push(i);
        count[i] = 1;
    }
}

let ptr = 0;
while (queue.length > ptr) {
    const node = queue[ptr++];
    for (const [adj, era] of graph[node]) {
        --indegree[adj];
        count[adj] += era * count[node];
        if (!indegree[adj]) {
            queue.push(adj);
        }
    }
    if (graph[node].length) count[node] = -1;
}
let result = '';
for (let i = 1; i < N+1; i++) {
    if (count[i] !== -1) {
        result += i + ' ' + count[i] + '\n';
    }
}

console.log(result.trim());