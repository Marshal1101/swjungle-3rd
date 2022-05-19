// 15	43549522	6	marshal1101	165708	1656	node.js 	1595

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

function solution(input) {
    const K = +input[0];
    let caseNumber = 0;
    let i = 1;
    let result = '';
    while (caseNumber < K) {
        let isBinaryTree = 0;
        let [V, E] = input[i++].split(' ').map(Number);
        let graph = [];
        for (j = 0; j < V+1; j++) {
            graph.push([]);
        }
        for (j = 0; j < E; j++) {
            const [v1, v2] = input[i].split(' ').map(Number);
            graph[v1].push(v2);
            graph[v2].push(v1);
            i++;
        }
        let visited = new Array(V+1).fill(-1);
        for (let j = 1; j < V+1; j++) {
            if (visited[j] === -1) {
                // isBinaryTree *= dfs(graph, 1, visited);
                isBinaryTree += dfs(graph, j, visited);
                console.log(visited)
            }
        }
        caseNumber++;
        if (isBinaryTree) {
            result += 'NO\n'
        } else {
            result += 'YES\n'
        }
    }

    return result.trim();

    function dfs(graph, node, visited) {
        if (visited[node] !== -1) return 1;
        visited[node] = 1;
        const stack = [node];
        while (stack.length) {
            const v1 = stack.pop();
            for (const v2 of graph[v1]) {
                if (visited[v2] === -1) {
                    visited[v2] = 1 - visited[v1];
                    stack.push(v2);
                } else {
                    if (visited[v2] === visited[v1]) {
                        return 1;
                    }
                }
            }
        }

        return 0;
    }
}

console.log(solution(input));