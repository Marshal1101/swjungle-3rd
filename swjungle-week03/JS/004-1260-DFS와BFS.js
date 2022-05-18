// 116	43473680	6	marshal1101	20504	236	node.js 	1544

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(ele => ele.split(' ').map(Number));

// N: 정점, M: 간선, V: 시작점 
const [N, M, V] = input.shift();

// 그래프 생성
const graph = [];
for (let i = 0; i < N+1; i++) {
    graph.push([]);
}
for (let i = 0; i < M; i++) {
    const [v1, v2] = input[i];
    graph[v1].push(v2);
    graph[v2].push(v1);
}

function dfs(graph, v) {
    result = '';
    const visited = new Array(N+1).fill(false);

    // 작은 수부터 방문 위해 내림차순
    graph.forEach((node) => node.sort((a, b) => b - a));

    const stack = [v];
    while (stack.length) {
        const v1 = stack.pop();

        if (visited[v1] === false) result += `${v1} `;
        visited[v1] = true;
        for (const v2 of graph[v1]) {
            if (visited[v2] === false) {
                stack.push(v2);
            }
        }
    }
    
    return result.trim();
}

function bfs(graph, v) {
    result = '';
    const visited = new Array(N+1).fill(false);
    visited[v] = true;

    // 작은 수부터 방문 위해 오름차순
    graph.forEach((node) => node.sort((a, b) => a - b));

    const queue = [v];
    while (queue.length) {
        const v1 = queue.shift();
        result += `${v1} `;
        for (const v2 of graph[v1]) {
            if (visited[v2] === false) {
                queue.push(v2);
                visited[v2] = true;
            }
        }
    }
    
    return result.trim();
}

console.log(dfs(graph, V) + '\n' + bfs(graph, V));