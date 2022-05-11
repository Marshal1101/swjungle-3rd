const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

function biggistNumber(list) {
    const [N, K] = list[0].split(' ').map(Number);
    const numbers = list[1].split('').map(Number);

    // console.log(N, K, numbers)
    // 제거 가능한 숫자 개수
    let removedNumCnt = K;
    // 스택
    const stack = new Array();
    // 순회
    for (let i = 0; i < N; i++) {
        if (removedNumCnt > 0) {
            while (stack.length && stack[stack.length-1] < numbers[i] && removedNumCnt > 0) {
                stack.pop();
                removedNumCnt -= 1;
            }
            stack.push(numbers[i]);
        }
        else {
            stack.push(numbers.splice(i).join(''));
            break;
        }
        // console.log(stack, removedNumCnt);
    }

    if (removedNumCnt > 0) {
        const end = stack.length - removedNumCnt;
        return stack.slice(0, end).join('');
    }

    return stack.join('');
}

console.log(biggistNumber(input));