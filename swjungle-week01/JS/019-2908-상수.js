const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split(' ');

// console.log('input', input);

function sangSu(input) {
    const [A, B] = input;
    
    function reverseNum(number) {
        let res = '';
        for (let i = 2; i >= 0; i--) {
            res += number[i];
        }

        return res;
    }

    const revA = parseInt(reverseNum(A));
    const revB = parseInt(reverseNum(B));

    console.log(revA > revB ? revA : revB);
}

sangSu(input);



// 백준 최고 속도
// var input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');

var a = input[0];  
var b = input[1];

a = parseInt(a.split("").reverse().join(""));
b = parseInt(b.split("").reverse().join(""));
console.log((a > b)? a : b);