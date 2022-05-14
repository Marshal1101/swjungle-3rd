// 왜 안 돼?

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(Number);

class minHeap {
    constructor() {
        this.heap = [];
    }

    getlc = (x) => 2 * x + 1;
    getrc = (x) => 2 * x + 2;
    getp = (x) => Math.floor((x - 1) / 2);

    getRoot = () => {
        return this.heap[0] ? this.heap[0] : null;
    }

    getSize = () => {
        return this.heap.length;
    }

    heappush = (number) => {
        this.heap.push(number);
        this.heapifyUp();
    };

    heapifyUp = () => {
        let idx = this.heap.length - 1;
        const lastNode = this.heap[idx];

        while (true) {
            if (this.heap[this.getp(idx)] > lastNode) {
                this.heap[idx] = this.heap[this.getp(idx)];
                idx = this.getp(idx);
            } else break;
        }

        this.heap[idx] = lastNode;
    };

    heappop = () => {
        const firstNode = this.heap[0];
        if (this.heap.length === 0) return;
        if (this.heap.length === 1) this.heap = [];
        else {
            this.heap[0] = this.heap.pop();
            this.heapifyDown();
        }
        return firstNode;
    };

    heapifyDown = () => {
        const len = this.heap.length;
        const firstNode = this.heap[0];
        let idx = 0;

        while (this.getlc(idx) < len) {
            const leftChild = this.getlc(idx);
            const rightChild = this.getrc(idx);
            const biggerChild =
                this.heap[rightChild] &&
                this.heap[rightChild] < this.heap[leftChild]
                    ? rightChild
                    : leftChild;

            if (this.heap[biggerChild] < firstNode) {
                this.heap[idx] = this.heap[biggerChild];
                idx = biggerChild;
            } else break;
        }

        this.heap[idx] = firstNode;
    };
}

function solution(input) {
    let result = '';
    const N = +input[0];
    const over = new minHeap();
    const down = new minHeap();

    for(let i = 1; i <= N; i++) {
        const number = +input[i];
        if (down.getSize() > over.getSize()) {
            over.heappush(number);
        }
        else down.heappush(-number);
        if (over.getSize() === 0) result +=`${-down.getRoot()}\n`
        else{
            if (-down.getRoot() > over.getRoot()) {
                const temp = -down.heappop();
                down.heappush(-over.heappop());
                over.heappush(temp);
            }
            result +=`${-down.getRoot()}\n`
        }
    }

    return result.trim();
}

console.log(solution(input));