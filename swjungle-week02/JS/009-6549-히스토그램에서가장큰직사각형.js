const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

const testList = input.map((test) => test.split(' ').map(Number))
// console.log(testList);
function histogram(list) {
    const N = list[0];
    const rect = [0, ...list.splice(1), 0];
    checked = [0];
    area = 0;
    // console.log('N', N, 'rect', rect, 'checked[checked.length-1]', checked[checked.length-1]);

    for (let i = 1; i < N+2; i++) {
        while (checked && rect[checked[checked.length-1]] > rect[i]) {
            const curHeight = checked.pop();
            area = Math.max(area, (i - 1 - checked[checked.length-1]) * rect[curHeight]);
        }
        checked.push(i);
    }

    return area;
}

let k = 0;
while (1) {
    if (!testList[k][0]) break;
    
    console.log(histogram(testList[k]));
    
    k++;
}