// 33	43732579	6	marshal1101	139616	864	node.js 	2396

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

// console.log(input)

function solution(input) {
    const [M, N, H] = input[0].split(' ').map(Number);
    const boxes = [];
    for (let k = 0; k < H; k++) {
        boxes[k] = [];
        for (let j = N * (k) + 1; j < N * (k + 1) + 1; j++) {
            boxes[k].push(input[j].split(' '));
        }
    }

    // console.log(boxes)

    let q = [];
    let red = 0;
    let empty = 0;
    for (let k = 0; k < H; k++) {
        for (let j = 0; j < N; j++) {
            for (let i = 0; i < M; i++) {
                if (boxes[k][j][i] === '-1') {
                    boxes[k][j][i] = 1;
                    empty++;
                }
                if (boxes[k][j][i] === '1') {
                    boxes[k][j][i] = 1;
                    q.push([k, j, i]);
                    red++;
                }
            }
        }
    }

    let total = (M * N * H) - empty;
    let green = total - red;
    if (total === red) return 0;
    if (total === green) return -1;
    // console.log('total, red, green', total, red, green)

    let day = 0;
    let turnToRed = 0;
    while (q.length) {
        let nextQ = [];
        // console.log('q', q, 'nextQ', nextQ)
        for (const [z, y, x] of q) {
            // console.log('zyx', z, y, x, turnToRed)
            if (z - 1 > -1 && boxes[z - 1][y][x] === '0') {
                boxes[z - 1][y][x] = 1;
                nextQ.push([z - 1, y, x]);
                turnToRed++;
            }
            if (z + 1 < H && boxes[z + 1][y][x] === '0') {
                boxes[z + 1][y][x] = 1;
                nextQ.push([z + 1, y, x]);
                turnToRed++;
            }
            if (y - 1 > -1 && boxes[z][y - 1][x] === '0') {
                boxes[z][y - 1][x] = 1;
                nextQ.push([z, y - 1, x]);
                turnToRed++;
            }
            if (y + 1 < N && boxes[z][y + 1][x] === '0') {
                boxes[z][y + 1][x] = 1;
                nextQ.push([z, y + 1, x]);
                turnToRed++;
            }
            if (x - 1 > -1 && boxes[z][y][x - 1] === '0') {
                boxes[z][y][x - 1] = 1;
                nextQ.push([z, y, x - 1]);
                turnToRed++;
            }
            if (x + 1 < M && boxes[z][y][x + 1] === '0') {
                boxes[z][y][x + 1] = 1;
                nextQ.push([z, y, x + 1]);
                turnToRed++;
            }
        }
        // console.log('boxes', boxes)
        // console.log('nextQ', nextQ)
        day++;
        if (green === turnToRed) return day;
        q = nextQ;
    }
    return -1;
}

console.log(solution(input));