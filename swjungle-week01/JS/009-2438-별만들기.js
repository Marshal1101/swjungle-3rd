const fs = require('fs');
const N = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();
// console.log('N', N);

function makeStarLine(num) {
    let star = '';
    for (let i = 1; i <= num; i++) {
        for (let j = 0; j < i; j++) {
            star += '*';
        }
        console.log(star);
        star = '';
    }
}

makeStarLine(N);