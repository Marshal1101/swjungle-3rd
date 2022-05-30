const input = require('fs').readFileSync(
    'test.txt'
).toString().trim();

function zeroOneTile(input) {
    const N = +input;
    const dp = [BigInt(0), BigInt(1), BigInt(2), BigInt(2)];
    if (N == 1) return 1;
    if (N == 2) return 2;
    for (let i = 3; i < N+1; i++) {
        dp[3] = (dp[2] + dp[1]) % BigInt(15746);
        [dp[2], dp[1]] = [dp[3], dp[2]];
    }
    return dp[3];
}

console.log(zeroOneTile(input).toString());