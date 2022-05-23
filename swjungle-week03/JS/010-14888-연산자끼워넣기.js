/* 등수	제출 번호	시도	아이디	메모리	시간	언어	코드 길이
    7	43567575	1	marshal1101	10880	188	node.js 	819 */

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const N = +input[0];
const A = input[1].split(' ').map(Number);
const pmtd = input[2].split(' ').map(Number);

let max = -1000000000;
let min = 1000000000;

function calculus(result, cnt, p, m, t, d) {
    if (cnt === N) {
        if (result > max) max = result;
        if (result < min) min = result;
    }

    if (p < pmtd[0]) {
        calculus(result + A[cnt], cnt+1, p+1, m, t, d);
    }

    if (m < pmtd[1]) {
        calculus(result - A[cnt], cnt+1, p, m+1, t, d);
    }

    if (t < pmtd[2]) {
        calculus(result * A[cnt], cnt+1, p, m, t+1, d);
    }

    if (d < pmtd[3]) {
        calculus(parseInt(result / A[cnt]), cnt+1, p, m, t, d+1);
    }
}

calculus(A[0], 1, 0, 0, 0, 0);
console.log(max + '\n' + min);