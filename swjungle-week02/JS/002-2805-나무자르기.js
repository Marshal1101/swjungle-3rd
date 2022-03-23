const input = require('fs').readFileSync(
	'/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week02/JS/test.txt'
).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const trees = input[1].split(' ').map(Number).sort((a, b) => a - b);
// console.log('N', 'M', 'trees', N, M, trees);

function binarySearch(N, M, trees) {
    let top = trees[N-1]
    let bottom = 0;
    let maxHeight = 0;
    while (bottom <= top) {
        let mid = parseInt((bottom + top) / 2);
        let cutLength = 0;
        trees.forEach((tree) => {
            if (mid < tree) {
                cutLength += (tree - mid);
            }
        })
        if (cutLength === M) return mid;
        else if (cutLength > M) {
            bottom = mid + 1;
            if (mid > maxHeight) maxHeight = mid;
        }
        else {
            top = mid - 1;
        }
    }

    return maxHeight;
}

console.log(binarySearch(N, M, trees));