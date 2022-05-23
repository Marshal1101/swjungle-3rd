// 1	43592736	2	marshal1101	12048	192	node.js 	1491

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const mid = (N+1) / 2;
const heavierThanIdx = Array(N+1);
const lighterThanIdx = Array(N+1);
for (let i = 1; i < N+1; i++) {
    heavierThanIdx[i] = [];
    lighterThanIdx[i] = [];
}
for (let i = 1; i < M+1; i++) {
    const [heavy, light] = input[i].split(' ').map(Number);
    heavierThanIdx[light].push(heavy);
    lighterThanIdx[heavy].push(light);
}

// console.log('heavierThanIdx', heavierThanIdx)
// console.log('lighterThanIdx', lighterThanIdx)
const heavyCheck = Array(N+1).fill(0);
const lightCheck = Array(N+1).fill(0);

let visited = Array(N+1).fill(false);
for (let i = 1; i < N+1; i++) {
    visited = Array(N+1).fill(false);
    heavyCheck[i] += dfs(i, heavierThanIdx);
    visited = Array(N+1).fill(false);
    lightCheck[i] += dfs(i, lighterThanIdx);
}
console.log(heavyCheck)
console.log(lightCheck)
let cnt = 0;
cnt += checkCnt(heavyCheck, N, mid);
cnt += checkCnt(lightCheck, N, mid);
console.log(cnt);

function checkCnt(chkList, n, mid) {
    let ans = 0;
    for (let i = 1; i < n+1; i++) {
        if (chkList[i] > mid) ans++; 
    }

    return ans;
}

function dfs(node, graph) {
    let ans = 0;
    const stack = [node];
    while (stack.length) {
        const node = stack.pop();
        if (visited[node] !== true) {
            visited[node] = true;
            ans++;
            for (const adj of graph[node]) {
                if (visited[adj] === false) {
                    stack.push(adj);
                }
            }
        }
    }

    return ans;
}