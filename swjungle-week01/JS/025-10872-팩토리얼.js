const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();

function factorial(number) {
    let res = 1;
    for (let i = 1; i <= number; i++) {
        res *= i;
    }

    return res;
}

console.log(factorial(input));