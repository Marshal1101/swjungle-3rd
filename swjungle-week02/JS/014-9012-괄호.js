// 54	41511517	2	marshal1101	9344	124	node.js 	814

const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

function bracket(input) {
    const result = [];
    const N = +input[0];
    let arr;
    for (let i = 1; i <= N; i++) {
        arr = input[i];
        const T = arr.length;
        let ptr = 0;
        if (arr[0] !== '(') {
            result.push('NO');
            continue;
        }
        // const stack = [];
        for (let j = 0; j < T; j++) {
            if (arr[j] === '(') {
                // stack.push(1);
                ptr += 1;
            } else if (arr[j] === ')') {
                // stack.pop();
                ptr -= 1;
            }
            if (ptr < 0) {
                break;
            }
        }
        if (ptr === 0) {
            result.push('YES')
        } else {
            result.push('NO')
        }
    }

    return result;
}

console.log(bracket(input).join('\n'));