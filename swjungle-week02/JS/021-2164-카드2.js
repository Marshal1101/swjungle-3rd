// 23	43204807	1	marshal1101	32868	220	node.js 	479

const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim();

function solution(num) {
    let ptr = 0;
    let len = +num;
    const data = new Array(+num).fill(1).map((value, index) => value + index);

    while (len > 1) {
        data.push(data[++ptr]);
        ptr++;
        len--;
    }

    return data[ptr];
}

console.log(solution(input));