// 2	43724554	1	marshal1101	12948	212	node.js 	1324

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const N = +input[0];
const miro = [];
for (let i = 1; i < N+1; i++) {
    miro.push(input[i].split(''));
}

// console.log(N, miro);

function bfs(N, miro) {
    const blackCostMap = [];
    for (let i = 0; i < N; i++) {
        blackCostMap[i] = Array(N).fill(-1);
    }
    const queue = [[0, 0, 0]];
    blackCostMap[0][0] = 0;
    let ptr = 0;

    const dy = [1, 0, -1, 0];
    const dx = [0, 1, 0, -1]; 

    while (queue.length > ptr) {
        const [y, x, cost] = queue[ptr++];
        if (cost > blackCostMap[y][x]) continue;
        for (let i = 0; i < 4; i++) {
            const ny = y + dy[i];
            const nx = x + dx[i];
            if (ny >= 0 && ny < N && nx >= 0 && ny < N) {
                const expCost = (miro[ny][nx] === '0' ? cost + 1 : cost);
                if (blackCostMap[ny][nx] === -1) {
                    blackCostMap[ny][nx] = expCost;
                    queue.push([ny, nx, expCost]);
                } else {
                    if (expCost < blackCostMap[ny][nx]) {
                        blackCostMap[ny][nx] = expCost;
                        queue.push([ny, nx, expCost]);
                    }
                }
            }
        }
    }

    return blackCostMap[N-1][N-1];
}

console.log(bfs(N, miro));