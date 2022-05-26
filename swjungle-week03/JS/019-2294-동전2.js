let [nk, ...coins] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const [n, k] = nk.split(' ').map(Number);
coins = coins.map(Number);

// console.log(n, k, coins)

let queue = [[0, 0]];
let minEra = Number.MAX_SAFE_INTEGER;

// console.log(queue)
while (queue.length) {
    queue = bfs(0, 0);
}
if (minEra < Number.MAX_SAFE_INTEGER) console.log(minEra);
else console.log(-1);

function bfs() {
    const queue = [v, e];
    const newQ = [];
    let temp = 0;
    for (const [value, era] of queue) {
        if (era > minEra) continue;
        // console.log('value era', value, era);
        for (let i = 0; i < n; i++) {
            temp = value + coins[i];
            // console.log('temp', temp)
            if (temp < k) newQ.push([temp, era + 1]);
            else if (temp === k) {
                if (era + 1 < minEra) minEra = era + 1;
            }
        }
    }

    return newQ;
}