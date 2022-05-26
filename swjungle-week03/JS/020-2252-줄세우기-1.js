// 30	43817818	1	marshal1101	56984	432	node.js 	815

let [nm, ...arr] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');
arr = arr.map((list) => list.split(' ').map(Number));
const [N, M] = nm.split(' ').map(Number);
const graph = Array.from({ length : N+1 }, () => []);
arr.forEach((arrow) => graph[arrow[0]].push(arrow[1]));
const indegree = new Array(N + 1).fill(0);
arr.forEach((arrow) => indegree[arrow[1]] += 1);

// console.log('arr', arr);
// console.log('graph', graph);
// console.log('indegree', indegree);

const queue = [];
for (let i = 1; i < N + 1; i++) {
    if (!indegree[i]) queue.push(i);
}
// console.log('queue', queue)
let result = '';
let cnt = 0;
let ptr = 0;
while (queue.length > ptr) {
    const node = queue[ptr++];
    // console.log(node)
    result += node + ' ';
    if (graph[node]) {
        for (const adj of graph[node]) {
            --indegree[adj];
            if (!indegree[adj]) queue.push(adj);
        }
    }
    cnt++;
}

console.log(result.trim());