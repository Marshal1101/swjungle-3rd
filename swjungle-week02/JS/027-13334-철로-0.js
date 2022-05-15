// https://www.acmicpc.net/source/30562977

const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

class Path {
    constructor(pos1, pos2) {
        if (pos1 < pos2) {
            this.start = pos1;
            this.end = pos2;
        } else {
            this.start = pos2;
            this.end = pos1;
        }
    }
}

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

const n = +input[0];
const hos = input
    .slice(1, 1 + n)
    .map((str) => new Path(...str.split(" ").map(Number)));
const d = +input[n + 1];

const heap = new Heap((a, b) => a < b);
let max = 0;

hos.sort((a, b) => a.end - b.end)
console.log(hos)

hos.forEach((path) => {
        const from = path.end - d;
        if (path.start < from) return;

        while (heap.size > 0 && heap.peak() < from) heap.poll();
        heap.add(path.start);

        if (heap.size > max) max = heap.size;
    });

console.log(max);