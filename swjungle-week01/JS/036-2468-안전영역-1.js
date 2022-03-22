// 백준 빠른 풀이

"use strict";

function getMaxH(arr, n) {
    var max = 0;

    for (var i = 0; i < n; i++) {
        for (var j = 0; j < n; j++) {
            if (arr[i][j] > max) {
                max = arr[i][j];
            }
        }
    }

    return max;
}

function visit(arr, n, h, x, y, visited, directions) {
    if (x < 0 || y < 0 || x >= n || y >= n) {
        return;
    }

    if (arr[x][y] <= h || visited[x][y]) {
        return;
    }

    visited[x][y] = true;

    for (var i = 0; i < directions.length; i++) {
        visit(arr, n, h, x + directions[i][0], y + directions[i][1], visited, directions);
    }
}

var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

var n = parseInt(input.shift());
input = input.map(function (x) {
    return x.split(' ').map(function (y) {
        return parseInt(y);
    });
});
var ans = 1;
var maxH = getMaxH(input, n);
var visited = Array(n);
var directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

for (var i = 0; i < n; i++) {
    visited[i] = Array(n);
}

for (var _i = 1; _i <= maxH; _i++) {
    for (var j = 0; j < n; j++) {
        for (var k = 0; k < n; k++) {
            visited[j][k] = false;
        }
    }

    var cnt = 0;

    for (var _j = 0; _j < n; _j++) {
        for (var _k = 0; _k < n; _k++) {
            if (visited[_j][_k] || input[_j][_k] <= _i) {
                continue;
            }

            visit(input, n, _i, _j, _k, visited, directions);
            cnt++;
        }
    }

    if (cnt > ans) {
        ans = cnt;
    }
}

console.log(ans);
