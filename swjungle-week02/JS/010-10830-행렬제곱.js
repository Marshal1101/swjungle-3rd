const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

const [N, B] = input[0].split(' ').map(Number);
const matrix = input.splice(1).map((row => row.split(' ').map(Number)));

function matrixTime(N, matrix1, matrix2) {
    let tmpMetrix = Array.from(Array(N), ()=> new Array(N));
        for (let i = 0; i < N; i++) {
            for (let j = 0; j < N; j++) {
                let ans = 0;
                for (let k = 0; k < N; k++) {
                    ans += matrix1[i][k] * matrix2[k][j]
                }
                tmpMetrix[i][j] = ans % 1000;
            }
        }
    return tmpMetrix;
}

function divideThousand(matrix) {
    return matrix.map((row => row.map(num => num % 1000)));
}

function divideExpo(N, B, matrix) {
    if (B === 1) return divideThousand(matrix);
    else if (B === 2) return matrixTime(N, matrix, matrix);
    else {
        let temp = divideExpo(N, parseInt(B/2), matrix);
        if (B % 2 === 0) {
            return matrixTime(N, temp, temp);
        }
        else {
            return matrixTime(N, matrixTime(N, temp, temp), matrix);
        }
    }
}

const res = divideExpo(N, B, matrix);
// console.log(res.map((row) => row.join(" ")).join("\n"));
res.forEach((row) => console.log(row.join(' ')));