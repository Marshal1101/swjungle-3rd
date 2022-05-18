// 73	43474957	1	marshal1101	115232	936	node.js 	879

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(ele => ele.split(' ').map(Number));

const [N, M] = input.shift();
const graph = [];
for (let i = 0; i < N+1; i++) {
    graph.push([]);
}
for (let i = 0; i < M; i++) {
    const [v1, v2] = input[i];
    graph[v1].push(v2);
    graph[v2].push(v1);
}

function bfs(v) {
    visited[v] = true;

    const queue = [v];
    while (queue.length) {
        const v1 = queue.shift();
        for (const v2 of graph[v1]) {
            if (visited[v2] === false) {
                queue.push(v2);
                visited[v2] = true;
            }
        }
    }
    
    return 1;
}

let count = 0;
const visited = new Array(N+1).fill(false);
for (let i = 1; i < N+1; i++) {
    if (visited[i] === false) {
        count += bfs(i);
    }
}

console.log(count);