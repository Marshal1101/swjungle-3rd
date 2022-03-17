const fs = require('fs');
const [C, ...arr] = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
// console.log('C', C, 'arr', arr);

function checkAboveAverage(test) {
    const [n, ...points] = test.split(' ');
    const len = points.length;
    let total = points.reduce((sum, value) => sum + parseInt(value), 0);
    const avg = total / len;
    let count = 0;
    points.forEach((value) => {
        if (parseInt(value) > avg) {
            count += 1; 
        }
    });

    return (count / len * 100).toFixed(3) + '%';
}

for (let i = 0; i < C; i++) {
    console.log(checkAboveAverage(arr[i]));
}