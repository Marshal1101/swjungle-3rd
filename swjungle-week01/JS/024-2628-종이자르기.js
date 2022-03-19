const fs = require('fs');
const input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim().split('\n');
const [paperSize, cutCount, ...arr] = input;

// console.log('paperSize', paperSize, 'cutCount', cutCount, 'arr', arr);

const [width, height] = paperSize.trim().split(' ');
const rowList = Array(height).fill(0);
const columnList = Array(width).fill(0);
rowList[height] = 1
columnList[width] = 1

console.log('row', rowList, 'column', columnList);


for (let i = 0; i < cutCount; i++) {
    const [isColumnCut, cutPlace] = arr[i].split(' ');
    // console.log('isColumnCut', isColumnCut, 'cutPlace', cutPlace);
    if (isColumnCut === '0') {
        rowList[cutPlace] = 1;
    }
    else {
        columnList[cutPlace] = 1;
    }
}
// console.log('row', rowList, 'column', columnList);

function checker(rowList, columnList) {
    const rowLen = rowList.length;
    const columnLen = columnList.length; 
    let rowBar = 0
    let columnBar = 0
    const rowCutList = new Array();
    const columnCutList = new Array();
    let maxHeight = 0;
    let maxWidth = 0;
    for (let i = 0; i < rowLen; i++) {
        if (rowList[i] === 1) {
            const gab = i - rowBar;
            rowCutList.push(gab);
            if (gab > maxHeight) {
                maxHeight = gab;
            }
            rowBar = i;
        }
    }
    for (let i = 0; i < columnLen; i++) {
        if (columnList[i] === 1) {
            const gab = i - columnBar;
            columnCutList.push(gab);
            if (gab > maxWidth) {
                maxWidth = gab;
            }
            columnBar = i;
        }
    }
    // console.log('rowCutList', rowCutList, 'columnCutList', columnCutList);
    msqure = maxWidth * maxHeight
    return msqure
}

console.log(checker(rowList, columnList));