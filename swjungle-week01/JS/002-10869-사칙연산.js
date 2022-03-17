let fs = require('fs');
let input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split(' ');
// console.log('input', input);
let num = input.length;
// console.log('num', num);
let [a, b] = input;

function arithmetic(num, a, b) {
	console.log(parseInt(a) + parseInt(b));
	console.log(a - b);
	console.log(a * b);
	console.log(Math.floor(a / b));
	console.log(a % b);
}

arithmetic(num, a, b);