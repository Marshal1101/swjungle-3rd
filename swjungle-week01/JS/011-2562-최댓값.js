const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
// console.log('input', input);

function maxValueAndIndex(input) {
    const len = input.length;
    let maxValue = 0;
    let maxIndex = 0;
    for (let i = 0; i < len; i++) {
        if (maxValue < parseInt(input[i])) {
            maxValue = parseInt(input[i]);
            maxIndex = i + 1;
        }
    }
    console.log(maxValue);
    console.log(maxIndex);
}

maxValueAndIndex(input);