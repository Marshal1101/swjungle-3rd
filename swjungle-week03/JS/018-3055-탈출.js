// 14	43785677	12	marshal1101	11648	192	node.js 	2436

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const [R, C] = input[0].split(' ').map(Number);
const forest = [];
for (let i = 1; i < R+1; i++) {
    forest.push(input[i].split(''));
}

let end;
let waterQ = [];
let sQ = [];
for (let j = 0; j < R; j++) {
    for (let i = 0; i < C; i++) {
        if (forest[j][i] === '.') continue;
        else if (forest[j][i] === '*') waterQ.push([j, i]);
        else if (forest[j][i] === 'D') end = [j, i];
        else if (forest[j][i] === 'S') sQ.push([j, i]);
        else forest[j][i] = '*';
    }
}

function water() {
    let nextWaterQ = [];
    for (const [y, x] of waterQ) {
        if (y === end[0] && x === end[1]) continue;
        if (y-1 >= 0 && forest[y-1][x] !== '*') {
            forest[y-1][x] = '*';
            nextWaterQ.push([y-1, x]);
        }
        if (y+1 < R && forest[y+1][x] !== '*') {
            forest[y+1][x] = '*';
            nextWaterQ.push([y+1, x]);
        }
        if (x-1 >= 0 && forest[y][x-1] !== '*') {
            forest[y][x-1] = '*';
            nextWaterQ.push([y, x-1]);
        }
        if (x+1 < C && forest[y][x+1] !== '*') {
            forest[y][x+1] = '*';
            nextWaterQ.push([y, x+1]);
        }
    }
    if (forest[end[0]][end[1]] === '*') forest[end[0]][end[1]] = 'D';
    // console.log('forest after water \n', forest);
    return nextWaterQ;
}

function sMove() {
    let nextSQ = [];
    for (const [y, x] of sQ) {
        if (y-1 >= 0 && forest[y-1][x] !== 'S' && forest[y-1][x] !== '*') {
            forest[y-1][x] = 'S';
            nextSQ.push([y-1, x]);
        }
        if (y+1 < R && forest[y+1][x] !== 'S' && forest[y+1][x] !== '*') {
            forest[y+1][x] = 'S';
            nextSQ.push([y+1, x]);
        }
        if (x-1 >= 0 && forest[y][x-1] !== 'S' && forest[y][x-1] !== '*') {
            forest[y][x-1] = 'S';
            nextSQ.push([y, x-1]);
        }
        if (x+1 < C && forest[y][x+1] !== 'S' && forest[y][x+1] !== '*') {
            forest[y][x+1] = 'S';
            nextSQ.push([y, x+1]);
        }
    }
    // console.log('forest after S \n', forest);
    return nextSQ;
}

function solution() {
    let time = 1;
    let pointer = 0;
    while (sQ.length) {
        waterQ = water();
        sQ = sMove();
        if (forest[end[0]][end[1]] === 'S') return time;
        time ++;
    }
    if (forest[end[0]][end[1]] === 'S') return time;
    else return 'KAKTUS';
}

console.log(solution());