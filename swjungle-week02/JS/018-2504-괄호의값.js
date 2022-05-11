const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('');

function sumBracketPoint(list) {
    if (list.length === 1) return 0;

    // 괄호 값
    let point = 0;

    // 열린 괄호 개수 체크
    let openBracketCnt = 0;

    // 스택
    const stack = new Array();
    for (let i = 0; i < list.length; i++) {

        if (stack.length) {
            while (stack.length) {
                if (stack[stack.length-1] === '(') {
                    if (list[i] === ')') {
                        stack.pop();
                        if (point === 0) {
                            stack.push(2);
                        } else {
                            stack.push(point * 2);
                            point = 0;
                        }
                        openBracketCnt -= 1;
                    } else if (list[i] === ']') {
                        return 0;
                    } else {
                        stack.push(list[i]);
                        openBracketCnt += 1;
                    }
                    break;
                }
                else if (stack[stack.length-1] === '[') {
                    if (list[i] === ']') {
                        stack.pop();
                        if (point === 0) {
                            stack.push(3);
                        } else {
                            stack.push(point * 3);
                            point = 0;
                        }
                        openBracketCnt -= 1;
                    } else if (list[i] === ')') {
                        return 0;
                    } else {
                        stack.push(list[i]);
                        openBracketCnt += 1;
                    }
                    break;
                }
                else {
                    if (list[i] === '(' || list[i] === '[') {
                        stack.push(list[i]);
                        openBracketCnt += 1;
                        break;
                    }
                    else {
                        point += stack.pop();
                    }
                }
            }
        }
        else {
            stack.push(list[i]);
            openBracketCnt += 1;
        }
    }

    return openBracketCnt ? 0 : stack.reduce(((prev, curr) => prev + curr), 0);
}

console.log(sumBracketPoint(input));