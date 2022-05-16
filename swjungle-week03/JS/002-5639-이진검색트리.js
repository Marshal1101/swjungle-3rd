// 34	43402443	5	marshal1101	434288	1248	node.js 	624

const input = require('fs').readFileSync(
    'test.txt'   
).toString().trim().split('\n').map(Number);

function recur(list) {
    if (list.length < 2) return list[0];
    let res = '';
    const root = list[0];
    for (let i = 1; i < list.length; i++) {
        if (root < list[i]) {
            if (i !== 1) res += recur(list.slice(1, i)) + '\n';
            res += recur(list.slice(i, list.length)) + '\n';
            res += root + '\n';
            return res.trim(); 
        }
    }
    res += recur(list.slice(1, list.length)) + '\n';
    res += root + '\n';
    return res.trim(); 
}

console.log(recur(input));