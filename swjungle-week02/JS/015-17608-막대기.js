// 3	42247502	6	marshal1101	16408	204	node.js 	410	

const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

// console.log(input);

function bar(input) {
    let N = +input.shift();
    let count = 1;
    let currBar = +input.pop();
    N = N - 2;
    while (N >= 0) {
        // console.log(N, count, currBar, +input[N]);
        // 대수 비교 시 string 숫자들이면 ('11' < '9')식으로 에러 발생한다.
        if (+input[N] > currBar) {
            currBar = +input[N];
            count++;
        }
        input.pop()
        N--;
    }

    return count;
}

console.log(bar(input));