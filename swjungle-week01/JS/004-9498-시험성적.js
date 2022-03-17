const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();
// console.log('input', input);


function checkYourGrade(input) {
    const point = parseInt(input);
    if (point >= 90) return console.log('A');
    else if (point >= 80) return console.log('B');
    else if (point >= 70) return console.log('C');
    else if (point >= 60) return console.log('D');
    else return console.log('F');
}

checkYourGrade(input);