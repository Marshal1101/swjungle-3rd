const input = require('fs').readFileSync(
	'/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week02/JS/test.txt'
).toString().trim().split('\n');

const N = +input[0];
const pH = input[1].split(' ').map(Number).sort((a, b) => a - b);

function twoPointer(N, pH) {
    let left = 0;
    let right = N-1;
    let minGab =  Number.MAX_SAFE_INTEGER;
    let gab;
    let result = Array(2);
    while (left < right) {
        let leftValue = pH[left];
        let rightValue = pH[right];
        gab = leftValue + rightValue;
        if (gab === 0) {
            result[0] = leftValue;
            result[1] = rightValue;
            return result.join(' ');
        }
        if (Math.abs(gab) < minGab) {
            minGab = Math.abs(gab);
            result[0] = leftValue;
            result[1] = rightValue;
        }
        if (Math.abs(pH[left+1] + pH[right]) < Math.abs(pH[left] + pH[right-1])) {
            left++;
        }
        else {
            right--;
        }
    }

    return result.join(' ');
}

console.log(twoPointer(N, pH));