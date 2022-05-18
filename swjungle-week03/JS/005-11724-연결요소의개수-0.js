// https://www.acmicpc.net/source/13125790

var path = require('path');
var inputs = require('fs').readFileSync(path.resolve('/dev/stdin'), 'utf8').toString().trim().split('\n');
var ix, jx;
var check = [];
var list = [];
var N = +inputs[0].toString().split(' ')[0];
var resultCnt = 0;

for(ix = 1; ix <= N; ix++) {
    list[ix] = [];
}

for (ix = 1; ix < inputs.length; ix++) {
    var input = inputs[ix].toString().split(' ');
    list[+input[0]].push(+input[1]);
    list[+input[1]].push(+input[0]);
}

function dfs(node) {
    check[node] = true;
    if (!list[node]) {
        return;
    }
    for (var ix = 0; ix < list[node].length; ix++) {
        var next = list[node][ix];
        if (!check[next]) {
            dfs(next);
        }
    }
}

dfs(1);
resultCnt += 1;

for (ix = 1; ix <= N; ix++) {
    if (!check[ix])
    {
        dfs(ix);
        resultCnt += 1;
    }
}
console.log(resultCnt);