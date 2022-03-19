const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');

const [n, ...arr] = input;
// console.log('n', n, 'arr', arr);
function checkPrimeNumber(number) {
    const num = parseInt(number);
    if (num === 1) {
        return 0;
    }

    const numSqrt = parseInt(Math.sqrt(num));
    for (let i = 2; i <= numSqrt; i++) {
        if (num % i === 0) {
            return 0;
        }
    }

    return 1;
}

let res = 0;
const splArray = arr[0].split(' ');
for (let i = 0; i < n; i++) {
    res += checkPrimeNumber(splArray[i]);
}

console.log(res);