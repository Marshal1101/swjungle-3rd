const fs = require('fs');
const [N, ...input] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');

function bubbleSort(list) {
    const len = list.length;
    let temp;
    for (let i = 0; i < len-1; i++) {
        for (let j = len-1; j > i; j--) {
            if (Number(list[j-1]) > Number(list[j])) {
                temp = list[j-1];
                list[j-1] = list[j];
                list[j] = temp;
            }
        }
    }
    return list;
}

const res = bubbleSort(input);
let temp;
for (let k = 0; k < N; k++) {
    if (temp !== res[k])
        console.log(Number(res[k]));
        temp = res[k];
}