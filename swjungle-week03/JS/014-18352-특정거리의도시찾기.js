// 1	43699096	15	marshal1101	205968	1984	node.js 	1009

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

// N 노드 개수, M 연결 개수, K 최소 연결 개수, X 시작 노드
const [N, M, K, X] = input[0].split(' ').map(Number);
const graph = [];
for (let i = 1; i < N+1; i++) {
    graph[i] = [];
}
for (let i = 1; i < M+1; i++) {
    const [v1, v2] = input[i].split(' ').map(Number);
    graph[v1].push(v2);
}

/* 사랑합니다 */
function bfs(N, K, X) {
    const result = [];
    const visited = Array(N+1).fill(false);
    visited[X] = true;
    let ptr = 0;
    const queue = [[X, 0]];
    while (queue.length > ptr) {
        const [node, dist] = queue[ptr++];
        if (dist > K) continue;
        for (const adj of graph[node]) {
            if (visited[adj] !== true) {
                queue.push([adj, dist+1]);
                visited[adj] = true;
                if (dist+1 === K) result.push(adj);
            }
        }
    }
    
    return result.length ? result.sort((a, b) => a - b).join('\n') : -1;
}

console.log(bfs(N, K, X));