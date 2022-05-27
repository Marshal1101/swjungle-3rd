let [N, M, ...arr] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

N = +N;
M = +M;
const graph = Array(N+1).fill(null).map(ele => []);
const revGraph = Array(N+1).fill(null).map(ele => []);
const indegree = Array(N+1).fill(0);
const maxTime = Array(N+1).fill(0);
const visited = Array(N+1).fill(false);
for (let i = 0; i < M; i++) {
    const [v1, v2, hour] = arr[i].split(' ').map(Number);
    graph[v1].push([v2, hour]);
    indegree[v2]++;
    revGraph[v2].push([v1, hour]);
}
const [start, end] = arr[M].split(' ').map(Number);

function topologySort(start, end) {
    const queue = [start];
    let ptr = 0;
    while (queue.length > ptr) {
        const curCity = queue[ptr++];
        for (const [adj, hour] of graph[curCity]) {
            const expHour = maxTime[curCity] + hour;
            indegree[adj]--;
            if (expHour > maxTime[adj]) maxTime[adj] = expHour;
            if (!indegree[adj]) queue.push(adj);
        }
    }

    return maxTime[end];
}

function bfs(end) {
    const queue = [end];
    let pathCnt = 0;
    let ptr = 0;
    while (queue.length > ptr) {
        const curCity = queue[ptr++];
        if (!visited[curCity]) {
            visited[curCity] = true;
            for (const [adj, hour] of revGraph[curCity]) {
                if (maxTime[curCity] - maxTime[adj] === hour) {
                    queue.push(adj);
                    pathCnt++;
                }
            }
        }
    }

    return pathCnt;
}

console.log(topologySort(start, end) + '\n' + bfs(end));