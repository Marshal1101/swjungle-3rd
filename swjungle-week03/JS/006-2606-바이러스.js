// 54	43477575	1	marshal1101	9432	120	node.js 	809

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(ele => ele.split(' ').map(Number));

const N = +input[0];
const M = +input[1];
const graph = [];
for (let i = 0; i < N+1; i++) {
    graph[i] = [];
}
for (let i = 2; i < M+2; i++) {
    const [v1, v2] = input[i];
    graph[v1].push(v2);
    graph[v2].push(v1);
}

function bfs(graph, v) {
    result = 0;
    const visited = new Array(N+1).fill(false);
    visited[v] = true;
    const queue = [v];
    while (queue.length) {
        const v1 = queue.shift();
        result += 1;
        for (const v2 of graph[v1]) {
            if (visited[v2] === false) {
                queue.push(v2);
                visited[v2] = true;
            }
        }
    }
    
    return result-1;
}

console.log(bfs(graph, 1));