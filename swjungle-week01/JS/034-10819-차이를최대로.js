const fs = require('fs');
const [N, input] = fs.readFileSync(
    '/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt'
    ).toString().trim().split('\n');


function makeBigDifference(N, input) {
    const originList = input.split(' ');
    const caseList = new Array(N).fill(-1);
    const flagIndex = new Array(N).fill(0);
    let count = 0;
    let maxSum = 0;
    
    function sumList(N, caseList, originList) {
        let ans = 0;
        for (let i = 0; i < N-1; i++) {
            ans += Math.abs(originList[caseList[i]] - originList[caseList[i+1]]);
        }
        return ans;
    }

    function makeCase(i, originList) {
        for (let j = 0; j < N; j++) {
            if (!flagIndex[j]) {
                caseList[i] = j;
                if (i === N-1) {
                    count += 1;
                    const sum = sumList(N, caseList, originList);
                    if (sum > maxSum) {
                        maxSum = sum;
                    }
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
    console.log(maxSum);
}

makeBigDifference(N, input);



// result [ 5, 4, 3, 2, 1, 0 ] [ 5, 4, 3, 2, 1, 0 ] count 720 
// 각 결과들 push 했는데, 왜 죄다 같은 값으로 저장되어있지? => 얇은 복사를 했었기에