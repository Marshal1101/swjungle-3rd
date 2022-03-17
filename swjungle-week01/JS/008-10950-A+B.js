const fs = require('fs');
const [n, ...arr] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
// console.log('n', n, 'arr', arr);

function aPlusB(n, arr) {
    for (let i = 0; i < n; i++) {
        let [a, b] = arr[i].split(' ');
        console.log(parseInt(a) + parseInt(b));
    }
}

aPlusB(n, arr);