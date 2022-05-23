// 68	43594134	1	marshal1101	12996	196	node.js 	1077

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const miro = [];
for (let i = 0; i < N; i++) {
    miro[i] = input[i+1].split('');
}

bfs(0, 0, miro);
console.log(miro[N-1][M-1]);

function bfs(i, j, graph) {
    if (graph[i][j] !== '1') return 'this is not 1';

    graph[i][j] = 1;
    const queue = [[i, j]];
    let ptr = 0;
    while (queue.length > ptr) {
        const [y, x] = queue[ptr++];
        // console.log(miro)
        if (y-1 >= 0 && graph[y-1][x] === '1') {
            queue.push([y-1, x]);
            graph[y-1][x] = graph[y][x] + 1;
        }
        if (y+1 < N && graph[y+1][x] === '1') {
            queue.push([y+1, x]);
            graph[y+1][x] = graph[y][x] + 1;
        }
        if (x-1 >= 0 && graph[y][x-1] === '1') {
            queue.push([y, x-1]);
            graph[y][x-1] = graph[y][x] + 1;
        }
        if (x+1 < M && graph[y][x+1] === '1') {
            queue.push([y, x+1]);
            graph[y][x+1] = graph[y][x] + 1;
        }
    }
}