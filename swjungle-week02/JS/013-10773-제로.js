const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

function zero(input) {
    const N = +input[0]
    stack = [];
    let temp;
    for (let i = 1; i <= N; i++) {
        temp = +input[i];
        if (temp !== 0) {
            stack.push(temp);
        } else {
            stack.pop();
        }
    }
    return stack.reduce((a,b)=>a+b, 0);
}

console.log(zero(input));