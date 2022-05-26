let [[N, M], ...arr] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(el => el.split(' ').map(el2 => +el2));

const indegree= Array(N+1).fill(0);
const graph = Array(N+1).fill(null).map(ele => []);
arr.forEach((ele) => {
    graph[ele[0]].push(ele[1]);
    indegree[ele[1]] += 1;
})

function topologySort() {
    let result = '';
    const q = [];
    for (let i = 1; i < N+1; i++) {
        if (!indegree[i]) q.push(i);
    }

    let ptr = 0;
    while (q.length > ptr) {
        const node = q[ptr++];
        result += `${node} `;
        if (graph[node]) {
            for (const adj of graph[node]) {
                --indegree[adj];
                if (!indegree[adj]) q.push(adj);
            }
        }
    }
    console.log(result.trim());
}

topologySort();