const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

function topChecker(input) {
	const n = +input[0];
	const topHeightList = input[1].split(' ').map(Number);
	const result = Array(n).fill(0);

	let stack = [];
	for (let i = n - 1; i >= 0; i--) {
		while (stack.length && topHeightList[i] > topHeightList[stack[stack.length - 1]]) {
			result[stack.pop()] = i + 1;
		}
		stack.push(i);
	}

	return result;
}

console.log(topChecker(input).join(' '));