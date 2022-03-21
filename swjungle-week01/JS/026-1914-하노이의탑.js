const fs = require('fs');
let input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();

function hanoii(floor, start, end) {
    if (floor <= 1) {
        return `${start} ${end}\n`;
    }
    else {
        let res = '';
        const waypoint = 6 - start - end;
        res += hanoii(floor - 1, start, waypoint);
        res += hanoii(1, start, end);
        res += hanoii(floor - 1, waypoint, end);
        return res;
    }
}

function soulution(floor) {
    // 백준 9%에서 틀렸었다고 하는 이유 => 2**floor-1 이 아니라 왜 비트쉬프트로 해야함? 
    // Internet Explorer 가 **을 호환하지 않아서 같다?
    const K = (BigInt(1) << BigInt(floor)) - BigInt(1);
    console.log(String(K));
    if (floor <= 20) {
        console.log(hanoii(floor, 1, 3));
    }
}

soulution(Number(input));