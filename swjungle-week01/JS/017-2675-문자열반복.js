const fs = require('fs');
const [T, ...arr] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
// console.log('T', T, 'arr', arr);

function duplicateString(test) {
    const [R, S] = test.split(' ');
    // const word = String(S).split('');
    // console.log('R', R, 'S', S, 'word', word);
    const len = S.length;
    let res = '';
    for (let j = 0; j < len; j++) {
        for (let i = 0; i < R; i++) {
            res += S[j];
        }
    }
    console.log(res);
}

for (let i = 0; i < T; i++) {
    duplicateString(arr[i]);
}