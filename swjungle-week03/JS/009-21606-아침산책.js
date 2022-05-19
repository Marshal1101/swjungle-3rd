// 1	43551911	6	marshal1101	200	114748	996	node.js 	1344

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const N = +input.shift();
const A = input.shift().split('').map(Number);
const graph = [];
for (let i = 0; i < N+1; i++) {
    graph[i] = [];
}
for (const ele of input) {
    const [v1, v2] = ele.split(' ').map(Number);
    graph[v1].push(v2);
    graph[v2].push(v1);
}

const visited = new Array(N+1).fill(0);
let result = 0;
for (let i = 1; i < N+1; i++) {
    if (visited[i] === 0) {
        result += start(i);
    }
}

// 결과 출력
console.log(result);

function start(node) {
    let res = 0;
    if (A[node-1] === 1) {
        for (const adj of graph[node]) {
            if (visited[adj] === 0) {
                if (A[adj-1] === 0) {
                    res += DFS(adj);
                } else {
                    res += 1;
                }
            }
        }
    } else {
        res += DFS(node);
    }
    return res;
}

function DFS(node) {
    let ans = 0;
    visited[node] = 1;
    const stack = [node];
    while (stack.length) {
        const v1 = stack.pop();
        for (const v2 of graph[v1]) {
            if (visited[v2] === 0) {
                if (A[v2-1] === 0) {
                        visited[v2] = 1;
                        stack.push(v2);
                }
                else {
                    ans++;
                }
            }
        }
    }
    return ans > 1 ? ans * (ans-1) : 0;
}