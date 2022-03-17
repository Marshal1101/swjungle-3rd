const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();
// console.log('input =', input);

function guguDan(input) {
    const n = parseInt(input);
    for (let i = 1; i < 10; i++) {
        console.log(`${n} * ${i} = ${n * i}`);
    }
}

guguDan(input);