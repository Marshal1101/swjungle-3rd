const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();

function hanSu(strNum) {
    strNumArr = strNum.split('');
    len = strNumArr.length;
    if (len < 3) {
        return true;
    }
    else {
        const gab1 = strNumArr[0] - strNumArr[1];
        const gab2 = strNumArr[1] - strNumArr[2];
        if (gab1 === gab2) {
            return true;
        }
        else {
            return false;
        }
    }
}

const number =  parseInt(input);
let count = 0;
for (let i = 1; i <= number; i++) {
    const strNum = String(i);
    if (hanSu(strNum)) {
        count++;
    }
}

console.log(count);