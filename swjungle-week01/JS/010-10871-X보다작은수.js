const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
// console.log('input', input);

const [N, X] = input[0].split(' ');
const arr = input[1].split(' ');
// console.log('N', N, 'X', X, 'arr', arr);
function checkBelowX(n, x, arr) {
    let res = '';
    for (let i = 0; i < n; i++) {
        if (parseInt(x) > parseInt(arr[i])) {
            res += arr[i] + ' '
        }
    }
    console.log(res);
}

checkBelowX(N, X, arr);