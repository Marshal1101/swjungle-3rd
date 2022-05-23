// 21	43575169	1	marshal1101	65244	828	node.js 	2014

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n')

const [N, M] = input[0].split(' ').map(Number);
const sea = Array(N);

for (let i = 0; i < N; i++) {
    sea[i] = (input[i+1].split(' ').map(Number));
}

let ice = [];
for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        if (sea[i][j]) {
            ice.push([i, j, sea[i][j]]);
        }
    }
}

let brk = false;
let year = 0;
while (ice.length) {
    for (const [i, j, height] of ice) {
        sea[i][j] = height;
    }

    let nextIce = [];
    let nextWater = [];
    while (ice.length) {
        const [i, j, height] = ice.pop();
        let meltedCnt = 0
        if (i-1 >= 0 && sea[i-1][j] === 0) meltedCnt++;
        if (i+1 <= N && sea[i+1][j] === 0) meltedCnt++;
        if (j-1 >= 0 && sea[i][j-1] === 0) meltedCnt++;
        if (j+1 <= M && sea[i][j+1] === 0) meltedCnt++;

        let ans = height - meltedCnt;
        if (ans < 1) nextWater.push([i, j]);
        else {
            nextIce.push([i, j, ans]);
        }
    }

    for (const [i, j] of nextWater) {
        sea[i][j] = 0;
    }

    ice = nextIce;
    year++;
    if (checkIcebergCnt(ice) > 1) {
        brk = true;
        break;
    }
}

console.log((brk ? year : 0));

function checkIcebergCnt(ice) {
    let res = 0;
    for (const [i, j, height] of ice) {
        if (sea[i][j] !== 0) res += dfs(i, j);
    }

    return res;

    function dfs (i, j) {
        if (sea[i][j] === 0) return;
        const stack = [[i, j]];
        while (stack.length) {
            const [ci, cj] = stack.pop();
            if (sea[ci][cj] > 0) {
                sea[ci][cj] = 0;
                if (ci-1 >= 0 && sea[ci-1][cj] > 0) stack.push([ci-1, cj]);
                if (ci+1 <= N && sea[ci+1][cj] > 0) stack.push([ci+1, cj]);
                if (cj-1 >= 0 && sea[ci][cj-1] > 0) stack.push([ci, cj-1]);
                if (cj+1 <= M && sea[ci][cj+1] > 0) stack.push([ci, cj+1]);
            }
        }

        return 1;
    }
}