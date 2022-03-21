// 95% 자꾸 틀리냐

const fs = require('fs');
const [N, input] = fs.readFileSync(
    '/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt'
    ).toString().trim().split('\n');

// console.log('N', N, 'input', input);

function makeBigDifference(N, input) {
    const sortedList = input.split(' ').sort((a, b) => Number(b) - Number(a));
    // console.log('list', sortedList);
    let idxL = Math.floor(N/2)-1;
    let idxR = idxL + 1;
    let result = 0;
    while ( idxL >= 0 || idxR <= N-1) {
        if (idxL === 0 && idxR === N-1) {
            result += (Number(sortedList[idxL]) - Number(sortedList[idxR]));
            return result;
        }
        else if (idxL === 0) {
            result += (Number(sortedList[idxL]) - Number(sortedList[idxR]));
            result += (Number(sortedList[idxL]) - Number(sortedList[idxR+1]));
            return result;
        }
        else if (idxR === N-1) {
            result += (Number(sortedList[idxL-1]) - Number(sortedList[idxR]));
            result += (Number(sortedList[idxL-1]) - Number(sortedList[idxR-1]));
            return result;
        }
        result += (Number(sortedList[idxL]) - Number(sortedList[idxR+1]));
        // console.log('result', result, 'idxL', idxL, 'idxR', idxR);
        result += (Number(sortedList[idxL-1]) - Number(sortedList[idxR]));
        // console.log('result', result, 'idxL', idxL, 'idxR', idxR);
        idxL--
        idxR++
        // console.log('result', result, 'idxL', idxL, 'idxR', idxR);
    }
}

console.log(makeBigDifference(N, input));