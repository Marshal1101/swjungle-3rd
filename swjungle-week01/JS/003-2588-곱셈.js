const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
// console.log('input', input);
const num = input.length;
// console.log('num', num);
const [a, b] = input;

function multiplication(firstNum, secondNum) {
    let number = 0;
    let sumNum = 0;
    for (let i = 2; i >= 0; i--) {
        number = firstNum * secondNum[i]
        console.log(number);
        sumNum += number * (10**(2-i));
    }
    console.log(sumNum);
}

multiplication(a, b);