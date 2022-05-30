// 52	43865227	3	marshal1101	9332	128	node.js / 수정	335

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim();

function fibonacci(input) {
    const N = +input;
    const dp = [];
    dp[0] = BigInt(0);
    dp[1] = BigInt(1);
    for (let i = 2; i < N+1; i++) {
        dp[i] = dp[i-1] + dp[i-2];
        console.log(dp)
    }
    return dp[N];
}

console.log(fibonacci(input).toString());