// 왜 안 돼

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n')

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
        // curIdx = 힙 마지막 인덱스에서 시작
        let curIdx = this.items.push(item) - 1;
        let parentIndex = this.getParentIndex(curIdx);

        // bubble up
        while (
            parentIndex >= 0 &&
            this.comp(this.items[curIdx], this.items[parentIndex])
        ) {
            this.swap(curIdx, parentIndex);
            curIdx = parentIndex;
            parentIndex = this.getParentIndex(curIdx);
        }
    }

    poll() {
        if (this.size < 2) return this.items.pop();

        // 루트를 내보내고, 마지막 요소를 루트로 이동
        const item = this.peak();
        this.items[0] = this.items.pop();

        // curIdx = 힙 루트 인덱스에 시작
        let curIdx = 0;
        let leftIndex = this.getLeftChildIndex(curIdx);
        let rightIndex = this.getRightChildIndex(curIdx);

        // bubble down
        while (leftIndex < this.size) {
            const target =
                rightIndex < this.size &&
                    this.comp(this.items[rightIndex], this.items[leftIndex])
                    ? rightIndex
                    : leftIndex;

            if (this.comp(this.items[curIdx], this.items[target])) break;
            this.swap(curIdx, target);

            curIdx = target;
            leftIndex = this.getLeftChildIndex(curIdx);
            rightIndex = this.getRightChildIndex(curIdx);
        }

        return item;
    }
}

function soulution(input) {
    const N = +input[0];
    const d = +input[N+1];
    const arr = [];
    for (let i = 1; i <= N; i++) {
        const [h, o] = input[i].split(' ').map(Number);
        if (h > o) arr.push([o, h]);
        else arr.push([h, o]);
    }
    
    arr.sort((a, b) => a[1] - b[1]);
    
    const hq = new Heap((a, b) => a < b);
    let maxCnt = 0;
    for (const x of arr) {
        if (x[1] - x[0] > d) continue;

        // 이건 안 됨 왜?
        // while (hq.size > 0 && hq.peak()[0] + d < x[1]) {
        //     hq.poll();
        // }
        // hq.add(x);
        
        while (hq.size > 0 && hq.peak() + d < x[1]) {
            hq.poll();
        }
        hq.add(x[0]);
        maxCnt = Math.max(maxCnt, hq.size);
    }

    return maxCnt;
}

console.log(soulution(input));