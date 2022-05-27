// 백준 js로 풀이 오류

function solution(input) {
  const N = input[0];
  const arr = input.splice(1);
  // console.log(N)
  // console.log(arr)
  const graph = Array(N + 1).fill(null).map(ele => []);
  const indegree = Array(N + 1).fill(0);
  const result = Array(N + 1).fill(null);
  arr.forEach((line, idx) => {
    for (let i = 0; i < N; i++) {
      if (line[i]) {
        graph[i + 1].push(idx + 1);
        indegree[idx + 1]++;
      }
    }
  });
  graph.forEach((ele) => ele.sort((a, b) => a - b));
  // console.log('graph', graph)
  // console.log('result', result)
  // console.log('indegree', indegree)
  const queue = [];
  for (let i = 1; i < N + 1; i++) {
    if (!indegree[i]) {
      queue.push([i, null]);
    }
  }

  function comp(a, b) {
    if (a >= b) return [a, b];
    else return [b, a];
  }
  if (!queue.length) return -1;
  let ptr = 0;
  while (queue.length > ptr) {
    let [node, sub] = queue[ptr++];
    if (!sub) sub = node;
    // console.log('node, sub', node, sub)
    let newNode, newAdj;
    for (const adj of graph[node]) {
      --indegree[adj];
      [newNode, newAdj] = comp(sub, adj);
      if (!indegree[adj]) {
        queue.push([adj, newAdj]);
      }
    }
    result[node] = newNode ? newNode : node;
  }

  return result.splice(1).join(' ');
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input;
let list = [];
rl.on('line', function (line) {
  input = line;
  rl.close();
}).on("close", function () {
  // list = input.split(' ').map((el) => el); 
  list = input.split(' ').map((el) => parseInt(el)); // 입력값이 정수라면 parseInt로 형 변환
  solution(list);
  process.exit();
});