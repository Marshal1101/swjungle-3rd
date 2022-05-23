// 11	43704785	8	marshal1101	60208	496	node.js 	1184

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const N = +input[0];
const M = +input[1];
const graph = [];
for (let i=1; i < N+1; i++) {
    graph[i] = [];
}
for (let i = 2; i < M+2; i++) {
    const [v1, v2, cost] = input[i].split(' ').map(Number);
    graph[v1].push({dest: v2, cost: cost});
}
const [start, end] = input[M+2].split(' ').map(Number);

function bfs(N, graph, start, end) {
    const minCost = Array(N+1).fill(-1);
    minCost[start] = 0;
    const queue = [[start, 0]];
    let ptr = 0;
    while (queue.length > ptr) {
        const [city, paid] = queue[ptr++];
        if (paid > minCost[city]) continue;
        for (const bus of graph[city]) {
            const curCost = paid + bus.cost;
            if (minCost[bus.dest] === -1) {
                minCost[bus.dest] = curCost;
                queue.push([bus.dest, curCost]);
            } else {
                if (curCost < minCost[bus.dest]) {
                    minCost[bus.dest] = curCost;
                    queue.push([bus.dest, curCost]);
                }
            }
        }
    }

    return minCost[end];
}

console.log(bfs(N, graph, start, end));