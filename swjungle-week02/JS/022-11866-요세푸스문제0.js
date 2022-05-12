// 89	43222548	1	marshal1101	21116	204	node.js 	667

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
        for (let i = exPtr; i < ptr; i++) {
            data.push(data[i]);
        }
        result += `${data[ptr]}, `;
        exPtr = ptr + 1;
        len--;
    }
    ptr += K;
    for (let i = exPtr; i < ptr; i++) {
        data.push(data[i]);
    }
    result = '<' + result + `${data[ptr]}>`
    data.splice()
    return result;
}

console.log(solution(N, K));