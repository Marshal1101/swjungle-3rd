// https://www.acmicpc.net/source/13551046

function solution(N, K) {
    var answer = '';
    var circleArray = Array(N);
    var head = 0;
  
    for (var i = 0; i < N; i++) {
      circleArray[i] = i + 1;
    }
  
    while (circleArray.length > 0) {
      head += K - 1;
      head %= circleArray.length;
      if (answer) answer += ', ';
      answer += circleArray[head];
      circleArray.splice(head, 1);
    }
  
    return '<' + answer + '>';
  }

var input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
console.log(solution(parseInt(input[0]), parseInt(input[1])));