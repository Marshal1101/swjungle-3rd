const fs = require('fs');
const input = fs.readFileSync(
    '/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt'
    ).toString().trim().split('\n');

// console.log('input', input);

function soulution(input) {
    const list = input.map(value => Number(value));
    const selectedSeven = new Set()
    const flagIndex = new Array(9).fill(false);
    // console.log('list', list);
    let count = 0;

    function sevenDwarf(i, list) {
        for (let j = 0; j < 9; j++) {
            if (!selectedSeven.has(j)) {
                selectedSeven.add(j);
                if (selectedSeven.size === 7) {
                    count += 1;
                    const resList = Array.from(selectedSeven).map((value) => list[value]);
                    const res = resList.reduce((prev, curr) => prev + curr, 0);
                    // console.log('resList', resList);
                    // console.log('res', res);
                    if (res === 100) {
                        resList.sort((a, b) => a - b);
                        resList.forEach(value => console.log(value));
                        process.exit();
                    }
                    else {
                        count -= 1;
                        selectedSeven.delete(j);
                    }
                }
                else {
                    // flagIndex[j] = true;
                    // console.log('selectedSeven', selectedSeven)
                    sevenDwarf(i+1, list);
                    // flagIndex[j] = false;
                    selectedSeven.delete(j);
                }
            }
        }
    }
    sevenDwarf(0, list);
    // console.log('count', count);
}

soulution(input);