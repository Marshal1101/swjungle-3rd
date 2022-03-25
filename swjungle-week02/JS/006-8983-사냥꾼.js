const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

const [M, N, L] = input[0].split(' ').map(Number);
const hunters = input[1].split(' ').map(Number).sort((a, b) => a - b);
const animals = input.splice(2).map(value => value.split(' ').map(Number)).sort((a, b) => a[0] - b[0]);

console.log(M, N, L, hunters, animals);
// 동물 x좌표와 가장 가까운 사냥꾼이 동물을 사냥한다.
// 그 사냥꾼이 사냥이 불가하면 다른 사냥꾼도 불가하다.

function twoPointerHunt(M, hunters, N, animals, L) {
    let count = 0;
    let exHunter = 0;

    for (let i = 0; i < N; i++) {
        let mLeft = exHunter;
        let mRight = M-1; 
        let mid;
        while (mLeft <= mRight) {
            mid = parseInt((mLeft + mRight) / 2);
            if (animals[i][0] > hunters[mid]) {
                if (mid === M-1 || animals[i][0] < hunters[mid+1]) {
                    break;
                }
                mLeft = mid + 1;
            }
            else {
                mRight = mid - 1;
            }
            // console.log('l, r, m', mLeft, mRight, mid);
        }
        exHunter = mid;
        if (Math.abs(hunters[mid] - animals[i][0]) + animals[i][1] <= L) count++;
        else if (M > mid+1 && Math.abs(animals[i][0] - hunters[mid+1]) + animals[i][1] <= L) count++;
    }

    return count;
}

console.log(twoPointerHunt(M, hunters, N, animals, L));