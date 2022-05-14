const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(Number);

function solution(input) {
    const result = [];
    const heapArr = [];
    const N = +input[0];

    // 힙 만들기(left 이외는 이미 힙이어야 한다)
    function downHeap(arr, left, right) {
        if (left >= right) return;
        let temp = arr[left];     // 현재 루트 값
        let parent = left       // 부모 인덱스는 가장 좌측
        let child = null;       // 큰 자식 인덱스
        while (parent < (parseInt((right + 1) / 2))) {
            let cl = parent * 2 + 1;    // 왼쪽 자식 인덱스
            let cr = cl + 1;            // 오른쪽 자식 인덱스
            if (cr <= right && arr[cr] > arr[cl]) {
                child = cr;
            } else {
                child = cl;
            }
            // 부모 > 자식이면, 중단
            if (temp >= arr[child]) {
                break;
            }
            // 부모 < 자식이면, 자식이 부모가 됨
            arr[parent] = arr[child];
            parent = child;
        }
        arr[parent] = temp;
    }

    // 최대 힙 만들기
    function heapMaxsort(arr) {
        const n = arr.length;
        for (let i = parseInt((n-1)/2); i > -1; i--) {
            downHeap(arr, i, n-1);
        }
    }
    
    // 힙에서 루트 꺼내기
    function deleteHeap(arr) {
        if (arr.length < 1) {
            return 0;
        }
        let root = arr[0];
        arr[0] = arr[arr.length-1];
        arr.pop();
        heapMaxsort(arr, 0, arr.length-1);
        
        return root;
    }

    // 배열에 넣고 힙 만들기
    function insertHeap(arr, num) {
        arr.push(num);
        if (arr[0] < num) {
            heapMaxsort(arr, 0, arr.length-1)     
        }
    }

    // 시작
    for (let i = 1; i <= N; i++) {
        if (input[i] === 0) {
            result.push(deleteHeap(heapArr));
        }
        else {
            insertHeap(heapArr, input[i]);
        }
    }

    return result.join('\n');
}

console.log(solution(input));