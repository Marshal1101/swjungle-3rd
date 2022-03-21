const fs = require('fs');
const [N, ...input] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');

console.log(input.sort((a, b) => Number(a) - Number(b)).join('\n'));