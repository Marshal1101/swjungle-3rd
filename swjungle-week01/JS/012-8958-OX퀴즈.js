const fs = require('fs');
const [n, ...arr] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
console.log('input', n, arr);

function checkPoints(test) {
    let isRelay = false;
    let relayPoints = 0;
    let relayCount = 0;
    let i = 0;
    let len = test.length;
    while (i < len) {
        if (test[i] === 'O') {
            if (!isRelay) {
                isRelay = true;
            }
            relayCount += 1;
            relayPoints += relayCount;
        }
        else {
            isRelay = false;
            relayCount = 0;
        }

        i++;
    }
    console.log(relayPoints);
}

for (let i = 0; i < n; i++) {
    // console.log(arr[i]);
    checkPoints(arr[i]);
}