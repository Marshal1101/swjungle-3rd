const fs = require('fs');
const [N, input] = fs.readFileSync(
    '/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt'
    ).toString().trim().split('\n');

const result = new Array();
let count = 0;
function makeBigDifference(N, input) {
    const originList = input.split(' ');
    const caseList = new Array(N).fill(-1);
    const flagIndex = new Array(N).fill(0);

    function makeCase(i, originList) {
        for (let j = 0; j < N; j++) {
            if (!flagIndex[j]) {
                caseList[i] = j;
                if (i === N-1) {
                    count += 1;
                    console.log('flagIndex', flagIndex, 'caseList', caseList);
                    console.log(result.push(caseList));
                }
                else {
                    flagIndex[j] = true;
                    makeCase(i+1, originList);
                    flagIndex[j] = false;
                }
            }
        }
    }

    makeCase(0, originList);
    console.log(result[0] === result[700] ? 1 : 0)
}

makeBigDifference(N, input);
console.log('result', result[0], result[719], 'count', count);



// result [ 5, 4, 3, 2, 1, 0 ] [ 5, 4, 3, 2, 1, 0 ] count 720 
// 각 결과들 push 했는데, 왜 죄다 같은 값으로 저장되어있지?