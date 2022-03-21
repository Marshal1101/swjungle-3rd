const checkList = new Array(1000001).fill(0);
let N;
const fs = require('fs');
fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n')
.forEach((value, index) => {
    if (index === 0) {
        N = value;
    }
    else {
        checkList[value] += 1;
    }
})
let count = 0;
let breaker = 0;
for (let i = 0; i < 1000001; i++) {
    if (breaker === N) break;
    count = checkList[i];
    while (count > 0) {
        console.log(i);
        count -= 1;
        breaker += 1;
    }
}