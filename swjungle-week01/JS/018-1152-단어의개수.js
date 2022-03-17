const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split(' ');
console.log('input', input);

console.log(input[0] === "" ? 0 : input.length);