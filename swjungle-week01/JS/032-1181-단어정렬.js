const fs = require('fs');
const [N, ...input] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');

const res = input.sort((a, b) => {
    if (a.length === b.length) {
        return (a > b ? 1 : -1);
    }
    else {
        return a.length - b.length;
    }
});
let temp;
for (let i = 0; i < N; i++) {
    if (temp !== res[i]) {
        console.log(res[i]);
        temp = res[i];
    }
}