const fs = require('fs');
let input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split(' ');

function solution(input) {
    let [N, r, c] = input.map(ele => Number(ele));
    binaryResult = "";
        while (N > 0) {
            let J = Math.pow(2, N-1);
            if (r < J) {
                binaryResult += '0';
            } else {
                binaryResult += '1';
                r = r - J;
            }
            if (c < J) {
                binaryResult += '0';
            }
            else {
                binaryResult += '1';
                c = c - J;
            }
            N -= 1;
        }
    const decimalResult = parseInt(binaryResult, 2);
    console.log(decimalResult);
}

solution(input);