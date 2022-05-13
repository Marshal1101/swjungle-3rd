// 86	43222887	1	marshal1101	21112	200	node.js 	649	

const [N, K] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split(' ').map(Number);

function solution(N, K) {
    result = '';
    let len = N;
    let ptr = -1;
    let exPtr = 0;
    let data = new Array(+N).fill(1).map((value, index) => value + index);
    while (len > 1) {
        ptr += K;
        for (let i = ptr-(K-1); i < ptr; i++) {
            data.push(data[i]);
        }
        result += `${data[ptr]}, `;
        len--;
    }
    ptr += K;
    for (let i = ptr-(K-1); i < ptr; i++) {
        data.push(data[i]);
    }
    result = '<' + result + `${data[ptr]}>`
    return result;
}

console.log(solution(N, K));