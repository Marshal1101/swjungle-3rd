const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

function soulution(input) {
    const cards = input.map(value => value.split(' '));
    const len = cards.length;
    const isExchanged = new Array(len).fill(false);
    const wantingColor = new Array(len);
    let result = 0;

    for (let i = 0; i < len; i++) {
        if (cards[i][0] === cards[i][1] && cards[i][0] < cards[i][2] {
        }
            if (Math.min(...cards[i]) )
            wantingColor[i] = -1;
            continue;
            || cards[i][1] === cards[i][2] || cards[i][2] === cards[i][0]) {
        }
        let minColor = 31;
        for (let j = 0; j < 3; j++) {
            if (cards[i][j] < minColor) {
                wantingColor[i] = j;
            }
        }
    }

    for (let i = 0; i < len; i++) {
        if (!isExchanged && wantingColor !== -1) {
            for (let j = 0; j < len; j++) {
                if (i === j) continue;
                if (!isExchanged && wantingColor[j] !== -1) {
                    if (wantingColor[i] !== wantingColor[j]) {
                        cards[i][wantingColor[i]] += 1;
                        cards[i][wantingColor[j]] -= 1;
                        cards[j][wantingColor[j]] += 1;
                        cards[j][wantingColor[i]] -= 1;
                        isExchanged[i] = isExchanged[j] = true;
                    }
                }
            }
        }
    }

    for (let i = 0; i < len; i++) {
        let min = Math.min(...cards[i]);
        console.log(i, min)
        result += min;
    }

    return result;
}

console.log(soulution(input));