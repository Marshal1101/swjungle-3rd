// 크루스칼 시도

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(ele => ele.split(' ').map(Number));

class UnionFind {
    constructor(edges) {
        this.root = edges;
        this.rank = Array(edges.length+1).fill(0);
    }

    find(x) {
        if (this.root[x] === x) {
            return x;
        } else {
            return this.root[x] = this.find(this.root[x]);
        }
    }

    union(x, y) {
        x = this.find(x);
        y = this.find(y);

        if (x === y) {
            return;
        }

        if (this.rank[x] < this.rank[y]) {
            this.root[x] = y;
        } else {
            this.root[y] = x;

            if (this.rank[x] === this.rank[y]) {
                this.root[x]++;
            }
        }
    }
}

function kruskalMST(input) {
    let answer = 0;
    const [V, E] = input.shift();
    input.sort((a, b) => a[2] - b[2]);
    const root = new UnionFind(input);
    console.log(input)
    for (let i = 0; i < E; i++) {
        if (root.find(input[i][0]) == root.find(input[i][1])) continue;
        root.union(input[i][0], input[i][1]);
        answer += input[i][2];
    }

    return answer;
}

console.log(kruskalMST(input));