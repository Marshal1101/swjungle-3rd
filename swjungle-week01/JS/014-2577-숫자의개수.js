const fs = require('fs');
const [A, B, C] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
const num = A * B * C;
// console.log(A, B, C, num);

function checkUsedNumbers(strNumber) {
    const number = String(strNumber).split('');
    // console.log('number', number);
    const checkList = new Array(10).fill(0);
    number.forEach((value) => (checkList[value] += 1));
    // console.log('checkList', checkList);
    checkList.forEach((value) => console.log(value));
}

checkUsedNumbers(num);