// 6	43251517	2	marshal1101	11368	132	node.js 	2720

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

function snakeMovingTime(list) {
    const N = +list[0];
    const K = +list[1];

    // 보드 생성
    const metrix = [Array(N+2).fill(1)];
    for (let i = 0; i < N; i++) {
        let row = Array(N).fill(0);
        row.unshift(1);
        row.push(1);
        metrix.push(row);
    }
    metrix.push(Array(N+2).fill(1));

    // 사과 배치
    for (let i = 2; i < K+2; i++) {
        const [y, x] = list[i].split(' ');
        metrix[y][x] = -1;
    }

    // 명령 정보 저장
    const L = +list[K+2];
    const orders = []; 
    for (let i = K+3; i < K+3+L; i++) {
        const [time, turn] = list[i].split(' ');
        orders.push([+time, turn]);
    }

    // 방향 전환 함수
    function turnDir(curDir, turn) {
        switch (curDir) {
            case ('U') :
                if (turn === 'L') {
                    return 'L';
                } else {
                    return 'R';
                }
            case ('D') :
                if (turn === 'L') {
                    return 'R';
                } else {
                    return 'L';
                }
            case ('L') :
                if (turn === 'L') {
                    return 'D';
                } else {
                    return 'U';
                }
            case ('R') :
                if (turn === 'L') {
                    return 'U';
                } else {
                    return 'D';
                }
            default :
                console.log('turnDir error');
                break;
        }
    }

    // 시작(좌표 1,1 초기 방향 R우측)
    let time = 0;
    let x = 1;
    let y = 1;
    let dir = 'R';
    const snakeXY = [[1, 1]];

    while (snakeXY.length > 0) {
        time++;
        switch (dir) {
            case ('U') :
                y--;
                break;
            case ('D') :
                y++;
                break;
            case ('L') :
                x--;
                break;
            case ('R') :
                x++;
                break;
            default :
                console.log('direction error');
                break;
        }
        if (metrix[y][x] !== 1) {
            snakeXY.push([y, x]);
            if (metrix[y][x] === 0) {
                const [tY, tX] = snakeXY.shift();
                metrix[tY][tX] = 0;
            }
            metrix[y][x] = 1;
        }
        else {
            return time;
        }

        if (orders.length && time == orders[0][0]) {
            const turn = orders.shift()[1];
            dir = turnDir(dir, turn);
        }
    }
}

console.log(snakeMovingTime(input));