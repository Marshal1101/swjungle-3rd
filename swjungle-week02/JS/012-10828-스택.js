const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

const N = +input[0];
const stack = [];
const result = [];
let len = 0;
let i = 1;
while (i <= N) {
    switch(input[i]) {
        case 'pop':
            if (len === 0) {
                result.push('-1');
            } else {
                result.push(stack.pop());
                len--;
            }
            break;
        case 'size':
            result.push(len);
            break;
        case 'empty':
            if (!len) {
                result.push('1');
            } else {
                result.push('0');
            }
            break;
        case 'top':
            result.push(stack[stack.length - 1] || -1);
            break;
        default:
            stack.push(input[i].substring(5));
            len++;
            break;
	}

    i++;
}

console.log(result.join('\n'));