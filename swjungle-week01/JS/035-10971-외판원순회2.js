const fs = require('fs');
const [N, ...input] = fs.readFileSync(
    '/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt'
    ).toString().trim().split('\n');

function TSP(n, input) {
    const graph = input.map((value) => {
        return value.split(' ');
    })
    // console.log('graph', graph);
    const caseList = new Array(N).fill(-1);
    const flagIndex = new Array(n).fill(0);
    let minSum = Number.MAX_SAFE_INTEGER;
    let count = 0;

    function sumCost(n, caseList, graph) {
        let ans = 0;
        let tmp = 0;
        for (let i = 0; i < n-1; i++) {
            tmp = Number(graph[caseList[i]][caseList[i+1]]);
            if (tmp !== 0) ans += tmp;
            else return Number.MAX_SAFE_INTEGER;;
        }
        tmp = Number(graph[caseList[n-1]][caseList[0]]);
        if (tmp !== 0) ans += tmp;
        else return Number.MAX_SAFE_INTEGER;;
        return ans;
    }

    function makeCase(i, n, graph) {
        for (let j = 0; j < n; j++) {
            if (!flagIndex[j]) {
                caseList[i] = j;
                if (i === N-1) {
                    count += 1;
                    const sum = sumCost(n, caseList, graph);
                    if (sum < minSum) {
                        minSum = sum;
                    }
                }
                else {
                    flagIndex[j] = true;
                    makeCase(i+1, n, graph);
                    flagIndex[j] = false;
                }
            }
        }
    }
    makeCase(0, n, graph);
    console.log(minSum);
}

TSP(N, input);