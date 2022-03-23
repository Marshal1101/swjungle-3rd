const { start } = require('repl');

const input = require('fs').readFileSync(
	'/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week02/JS/test.txt'
).toString().trim().split('\n');

const [N, C] = input[0].split(' ').map(Number);
const houseX = input.splice(1).map(Number).sort((a, b) => a - b);

// console.log('N', N, 'C', C, 'houseX', houseX);

function minimalMax(N, C, houseX) {
    let left = 1;
    let right = houseX[N-1] - houseX[0];
    let maxDist = 0;
    while (left <= right) {
        let mid = parseInt((left + right) / 2);
        let startIdx = 0
        let nextIdx = 1;
        let count = 1;
        let dist;
        let isLeftUp = false;
        // console.log('left', left, 'right', right, 'mid', mid);
        while (nextIdx <= N-1) {
            dist = houseX[nextIdx] - houseX[startIdx];
            if (dist >= mid) {
                startIdx = nextIdx;
                count++;
                if (count >= C) {
                    maxDist = mid;
                    left = mid + 1;
                    isLeftUp = true;
                    break;
                }
            }
            // console.log('mid', mid, 'dist', dist, 'startIdx', startIdx, 'nextIdx', nextIdx, 'count', count);
            nextIdx++;
        }
        if (!isLeftUp) {
            right = mid - 1;
        }
        // console.log('mid', mid, 'left', left, 'right', right);
    }

    return maxDist;
}

console.log(minimalMax(N, C, houseX));