// 백준 js로 풀이 오류

'use strict';

let [n, ...arr] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(ele => ele.split('').map(Number));
const N = n[0];
console.log(N)
console.log(arr)
const graph = Array(N + 1).fill(null).map(ele => []);
const indegree = Array(N + 1).fill(0);
const result = Array(N + 1).fill(null);
arr.forEach((line, idx) => {
    for (let i = 0; i < N; i++) {
        if (line[i]) {
            graph[i+1].push(idx+1);
            indegree[idx+1]++;
        }
    }
});
graph.forEach((ele) => ele.sort((a, b) => a - b));
console.log('graph', graph)
console.log('result', result)
console.log('indegree', indegree)
const queue = [];
for (let i = 1; i < N+1; i++) {
    if (!indegree[i]) {
        queue.push([i, null]);
    }
}

function comp(a, b) {
    if (a >= b) return [a, b];
    else return [b, a];
}

console.log('queue', queue)
function topologySort() {
    if (!queue.length) return -1;
    while (queue.length) {
        let [node, sub] = queue.pop();
        if (!sub) sub = node;
        // console.log('node, sub', node, sub)
        let newNode, newAdj;
        for (const adj of graph[node]) {
            --indegree[adj];
            [newNode, newAdj] = comp(sub, adj);
            if (!indegree[adj]) {
                queue.push([adj, newAdj]);
                queue.sort((a, b) => a - b);
            }
        }
        result[node] = newNode ? newNode : node;
    }

    return result.slice(1).join(' ');
}

console.log(topologySort());