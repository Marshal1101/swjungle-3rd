// 1	42943234	4	marshal1101	152232	912	node.js 	1468

const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

function countCircle(input) {
    N = +input.shift();
    const points = new Array();

    // 원(열림:0, 닫힘:1), 좌표, 상태(이어지면 1 아니면 0), 이어진 원 지름 길이의 합  
    input.forEach(circle => {
        const [center, radius] = circle.split(' ').map(Number);
        points.push([0, center - radius, 0, 0]);
        points.push([1, center + radius, 0, 0]);
    })

    // 정렬
    points.sort((a, b) => b[0] - a[0]).sort((a, b)=> a[1] - b[1]);
    // console.log(points);

    // 스택
    const stack = new Array();
    let count = 1;

    for (let i = 0; i < points.length; i++) {
        if (points[i][0] === 0) {
            if (stack.length) {
                if (stack[stack.length-1][1] === points[i][1] || stack[stack.length-1][3] === points[i][1]) {
                    stack[stack.length-1][2] = 1;
                } else {
                    stack[stack.length-1][2] = 0;
                }
            }
            stack.push(points[i]);
        }
        else {
            let half = stack.pop();
            if (stack.length && stack[stack.length-1][2] === 1) {
                stack[stack.length-1][3] = points[i][1];
            }
            if (half[2] === 1 && half[3] === points[i][1]) {
                count++;
            }

            count++;
        }
    }

    return count;
}

console.log(countCircle(input));