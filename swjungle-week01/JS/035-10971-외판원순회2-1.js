// 백준 빠른 풀이

const [ n, ...nums ] = require('fs').readFileSync('./dev/stdin').toString().trim().split('\n')
const N = +n
const board = nums.map(v=>v.split(' ').map(Number))
let min = 10000000;

for(let i = 0; i < N; i++) {
  let res = salesman(i, i, 1<<i, 0);
  if (min > res) min = res;
}

console.log(min)

function salesman(start, pos, visited, dist) {
  if (visited == (1 << N) - 1) {
    if (board[pos][start] != 0){
      dist += board[pos][start]
      if (dist < min) min = dist
    }
    return;
  }
  for (let next = 0; next < N; next++) {
    if(!(visited & (1<<next)) && board[pos][next] != 0 && min > dist + board[pos][next]) {
      salesman(start, next, visited|(1<<next), dist+board[pos][next]);
    }
  }
}