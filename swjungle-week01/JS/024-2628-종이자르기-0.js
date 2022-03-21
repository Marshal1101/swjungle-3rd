const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
const [paperSize, cutCount, ...arr] = input;

// console.log('paperSize', paperSize, 'cutCount', cutCount, 'arr', arr);

function cutPaper(paperSize, cutCount, whereCutList) {
    const [width, height] = paperSize.split(' ');
    // console.log('width', width, 'height', height);
    const listRow = Array(1).fill(0);
    const listColumn = Array(1).fill(0);
    if (whereCutList.length !== 0) {
        for (let i = 0; i < cutCount; i++) {
            const [isColumnCut, cutPlace] = whereCutList[i].split(' ');
            if (parseInt(isColumnCut) === 0) {
                listRow.push(parseInt(cutPlace));
            }
            else {
                listColumn.push(parseInt(cutPlace));
            }
        }
    }
    // 9% 에서 오류 발생, 왜 안 되지? sort() 가 익스플로러에서 완전 호환 안 되는 것으로 보임
    listColumn.sort().push(parseInt(width));
    listRow.sort().push(parseInt(height));

    return [listRow, listColumn];
}

function checkBiggestScale(rowList, columnList) {
    const rowLen = rowList.length;
    const columnLen = columnList.length;
    let maxWidth = 1;
    let maxHeight = 1;
    for (let i = 1; i < rowLen; i++) {
        let gab = rowList[i] - rowList[i-1];
        // console.log(gab);
        if (gab > maxHeight) {
            maxHeight = gab;
        }
    }
    for (let i = 1; i < columnLen; i++) {
        let gab = columnList[i] - columnList[i-1];
        // console.log(gab);
        if (gab > maxWidth) {
            maxWidth = gab;
        }
    }

    return (maxWidth * maxHeight);
}

const [listRow, listColumn] = cutPaper(paperSize, cutCount, arr);
// console.log('listRow', listRow, 'listColumn', listColumn);
console.log(checkBiggestScale(listRow, listColumn));