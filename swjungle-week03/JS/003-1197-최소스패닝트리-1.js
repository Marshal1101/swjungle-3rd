// 프림 시도

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(ele => ele.split(' ').map(Number));

class Heap {
    constructor(comp) {
        this.items = [];
        this.comp = comp;
    }

    get size() {
        return this.items.length;
    }

    swap(a, b) {
        const temp = this.items[a];
        this.items[a] = this.items[b];
        this.items[b] = temp;
    }

    getParentIndex(index) {
        return Math.floor((index - 1) / 2);
    }

    getLeftChildIndex(index) {
        return index * 2 + 1;
    }

    getRightChildIndex(index) {
        return index * 2 + 2;
    }

    peak() {
        return this.items[0];
    }

    add(item) {
        let index = this.items.push(item) - 1;
        let parentIndex = this.getParentIndex(index);

        while (
            parentIndex >= 0 &&
            this.comp(this.items[index], this.items[parentIndex])
        ) {
            this.swap(index, parentIndex);
            index = parentIndex;
            parentIndex = this.getParentIndex(index);
        }
    }

    poll() {
        if (this.size < 2) return this.items.pop();

        const item = this.peak();
        this.items[0] = this.items.pop();

        let index = 0;
        let leftIndex = this.getLeftChildIndex(index);
        let rightIndex = this.getRightChildIndex(index);

        while (leftIndex < this.size) {
            const target =
                rightIndex < this.size &&
                    this.comp(this.items[rightIndex], this.items[leftIndex])
                    ? rightIndex
                    : leftIndex;

            if (this.comp(this.items[index], this.items[target])) break;
            this.swap(index, target);

            index = target;
            leftIndex = this.getLeftChildIndex(index);
            rightIndex = this.getRightChildIndex(index);
        }

        return item;
    }
}

const [V, E] = input.shift();
// 그래프 생성
const graph = Array();
for (let i = 0; i < V+1; i++) {
    graph.push([])
}
input.forEach(ele => {
    const [node1, node2, value] = ele;
    graph[node1].push([node2, value]);
    graph[node2].push([node1, value]);
})
console.log(graph)
const minHeap = new Heap((a, b) => a > b);
const visited = new Array(V+1).fill(false);
let dist = 0;
let cnt = 0;
minHeap.add([0, 1]);

while (cnt < V) {
    let [d, v2] = minHeap.poll();
    if (visited[v2] !== false) {
        visited[v2] = true;
        dist += d;
        cnt++;

        for (const way of graph[v2]) {
            if (visited[way[0]] !== false) {
                minHeap.add([[way[1], way[0]]])
            }
        }
    }
}