const [n, ...input] = require('fs').readFileSync(
	'/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt'
).toString().trim().split('\n');

const N = +n;
const graph = input.map(value => value.split(' ').map(Number));

function safeArea(N, graph) {
	const flagArea = Array.from(Array(N), () => Array(N).fill(1));
	let height = 0;
	let unsafeCnt = 0;
	let maxSafeArea = 0;
	let tempSafeArea;

	while (unsafeCnt < N * N) {
		flagArea.forEach((row, i) => {
			row.forEach((flag, j) => {
				if (flag && isUnsafe(i, j, graph)) {
					flagArea[i][j] = 0;
					unsafeCnt += 1;
				}
			});
		});

		tempSafeArea = checkSafeArea(N, flagArea);
		if (tempSafeArea > maxSafeArea) maxSafeArea = tempSafeArea;
		height += 1;
		// console.log(height, unsafeCnt, tempSafeArea, maxSafeArea);
	}

	function deepCopy(N, metrix) {
		const copy = Array.from(Array(N), () => Array(N));
		metrix.forEach((row, i) => {
			row.forEach((value, j) => copy[i][j] = value);
		})
		return copy;
	}

	function isUnsafe(i, j, graph) {
		return (height >= graph[i][j] ? true : false);
	};

	function checkSafeArea(N, flagArea) {
		const visited = deepCopy(N, flagArea);
		// console.log('visited', visited)

		function BFS(i, j) {
			if (!visited[i][j]) return 0;
			const queue = [[i, j]];
			while (queue[0]) {
				const [i, j] = queue.pop();
				// console.log(queue, i, j);
				if (visited[i][j]) {
					visited[i][j] = 0;
					if (i > 0 && visited[i - 1][j]) queue.push([i - 1, j]);
					if (i < N - 1 && visited[i + 1][j]) queue.push([i + 1, j]);
					if (j > 0 && visited[i][j - 1]) queue.push([i, j - 1]);
					if (j < N - 1 && visited[i][j + 1]) queue.push([i, j + 1]);
				}
			}
			return 1;
		};

		let count = 0;
		for (let i = 0; i < N; i++) {
			for (let j = 0; j < N; j++) {
				if (visited[i][j] !== 0) {
					count += BFS(i, j);
				}
				// console.log('count', count)
			}
		}

		return count;
	};

	return maxSafeArea;
}

console.log(safeArea(N, graph));