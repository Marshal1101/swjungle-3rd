const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

const N = +input[0];
const paper = input.splice(1).map(row => row.split(' ').map(Number));

// console.log('N', 'paper', N, paper);

let white = 0;
let blue = 0;

function divideAndConquer(n, startRow, startColumn, paper) {
    const color = paper[startRow][startColumn];
    const nextLen = parseInt(n/2);
    
    for (let i = startRow; i < startRow + n; i++) {
        for (let j = startColumn; j < startColumn + n; j++) {
            if (color !== paper[i][j]) {
                exhaustedSearch(nextLen, startRow, startColumn, paper);
                exhaustedSearch(nextLen, startRow, startColumn + nextLen, paper);
                exhaustedSearch(nextLen, startRow + nextLen, startColumn, paper);
                exhaustedSearch(nextLen, startRow + nextLen, startColumn + nextLen, paper);
                return;
            }
        }
    }
    
    color ? blue++ : white++;
}

divideAndConquer(N, 0, 0, paper)
console.log(white +'\n' + blue);