const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

const N = +input[0];
const numbers = input[1].split(' ').map(Number);

function LongestIncreasingSubsequence(N, numbers) {
    const dp = new Array(N).fill(1);

    for (let i = 1; i < N; i++) {
        let expDp = 0;
        for (let j = i; j >=0; j-- ) {
            if (numbers[i] > numbers[j] && (dp[j] > expDp)) {
                expDp = dp[j]; 
            }
        }
        dp[i] += expDp;
    }

    return Math.max(...dp);
}

console.log(LongestIncreasingSubsequence(N, numbers));