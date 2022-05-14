class Heap {
    constructor() {
        this.heap = [];
    }

    getlc = (x) => 2 * x + 1;
    getrc = (x) => 2 * x + 2;
    getp = (x) => Math.floor((x - 1) / 2);

    insert = (number) => {
        this.heap.push(number);
        this.heapifyUp();
    };

    heapifyUp = () => {
        let idx = this.heap.length - 1;
        const lastNode = this.heap[idx];

        while (true) {
            if (this.heap[this.getp(idx)] < lastNode) {
                this.heap[idx] = this.heap[this.getp(idx)];
                idx = this.getp(idx);
            } else break;
        }

        this.heap[idx] = lastNode;
    };

    delete = () => {
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
                this.heap[rightChild] > this.heap[leftChild]
                    ? rightChild
                    : leftChild;

            if (this.heap[biggerChild] > firstNode) {
                this.heap[idx] = this.heap[biggerChild];
                idx = biggerChild;
            } else break;
        }

        this.heap[idx] = firstNode;
    };
}