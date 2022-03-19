const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
const [n, ...arr] = input;
// console.log(n, arr);

function goldbachPartition(test) {

    function checkPrimeNumber(number) {
        const num = parseInt(number);
        if (num === 1) {
            return false;
        }
    
        const numSqrt = parseInt(Math.sqrt(num));
        for (let i = 2; i <= numSqrt; i++) {
            if (num % i === 0) {
                return false;
            }
        }
    
        return true;
    }

    const half = test / 2;
    let left, right;
    let gab = 0;    
    while (true) {
        left = half - gab;
        right = half + gab;
        if (checkPrimeNumber(left) && checkPrimeNumber(right)) {
            break;
        }
        gab += 1;
    }
    console.log(left, right);
}

for (let i = 0; i < n; i ++) {
    goldbachPartition(arr[i])
}