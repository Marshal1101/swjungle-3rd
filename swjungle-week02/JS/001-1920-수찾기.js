const input = require('fs').readFileSync(
	'/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week02/JS/test.txt'
).toString().trim().split('\n');

const N = +input[0];
const M = +input[2];
const ref = input[1].split(' ').map(Number).sort((a, b) => a - b);
const list = input[3].split(' ').map(Number);
const result = new Array(M).fill(0);

function binarySearch(target, M, ref, N) {
    for (let i = 0; i < M; i++) {
        let left = 0;
        let right = N - 1;
        while (true) {
            let mid = parseInt((left + right) / 2);
            if (ref[mid] === target[i]) {
                result[i] = 1;
                break;
            }
            else if (ref[mid] < target[i]) {
                left = mid + 1;
            }
            else {
                right = mid - 1; 
            }
            if (left > right) {
                break;
            }
        }
    }
}

binarySearch(list, M, ref, N);
console.log(result.join('\n'));

// 1. 결과를 join 아닌 for 출력하면 시간이 매우 많이 걸린다.
// result.forEach((value) => {
//     console.log(value);
// });

// 2. result.push()는 배열 갯수를 미리 선언하는 것보다 때에 따라 느리지 않다.
// 3. input변수들 생성할 때, destructuring 사용하면 배열을 새로 생성하는 것이라 느리다.