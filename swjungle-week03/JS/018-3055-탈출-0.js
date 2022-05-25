const fs = require("fs");
let [rc, ...arr] = fs.readFileSync("test.txt").toString().trim().split("\n");
const [r, c] = rc.split(" ").map(Number);
arr = arr.map(a => a.trim().split(""));

// console.log(arr)

let d, s;
let water = [];
let checkList = Array.from({ length: r }, () => new Array(c).fill(0));
let dx = [1, -1, 0, 0];
let dy = [0, 0, 1, -1];

console.log(checkList)

for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
        if (arr[i][j] == "D") {
            d = [i, j];
        } else if (arr[i][j] == "*") {
            water.push([i, j, 1]);
            checkList[i][j] = 1;
        } else if (arr[i][j] == "S") {
            s = [i, j, 0];
            checkList[i][j] = 1;
        }
    }
}

water.push(s);
let pointer = 0;
while (pointer < water.length) {
    let [x, y, z] = water[pointer++];
    if (z == 0) {
        if (x == d[0] && y == d[1]) {
            break;
        } else {
            for (let i = 0; i < 4; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];

                if (
                    0 <= nx &&
                    nx < r &&
                    0 <= ny &&
                    ny < c &&
                    !checkList[nx][ny] &&
                    (arr[nx][ny] == "." || arr[nx][ny] == "D")
                ) {
                    checkList[nx][ny] = checkList[x][y] + 1;
                    water.push([nx, ny, 0]);
                }
            }
        }
    } else {
        if (x == d[0] && y == d[1]) {
            checkList[x][y] = 0;
            break;
        } else {
            for (let i = 0; i < 4; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];

                if (0 <= nx && nx < r && 0 <= ny && ny < c && arr[nx][ny] == ".") {
                    arr[nx][ny] = "*";
                    water.push([nx, ny, 1]);
                }
            }
        }
    }
}

let answer = checkList[d[0]][d[1]];
console.log(answer > 0 ? answer - 1 : "KAKTUS");
