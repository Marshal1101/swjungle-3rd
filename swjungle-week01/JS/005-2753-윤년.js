const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();
console.log('input', input);

function isLeapYear(year) {
    if (year % 400 === 0) 
        return 1;
    else if (year % 100 === 0) 
        return 0;
    else if (year % 4 === 0)
        return 1;
    else 
        return 0;
}

console.log(isLeapYear(input));