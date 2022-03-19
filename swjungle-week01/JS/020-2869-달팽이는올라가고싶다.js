const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split(' ');

const A = parseInt(input[0]);
const B = parseInt(input[1]);
const V = parseInt(input[2]);

let day = parseInt(((V - B) / (A - B)));
if (((V - B) % (A - B)) === 0) {
    console.log(day);
}
else {
    console.log(day+1);
}