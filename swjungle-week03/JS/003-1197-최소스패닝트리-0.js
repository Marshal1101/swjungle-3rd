// https://www.acmicpc.net/source/42263997

const fs = require('fs');

let input = fs.readFileSync('test.txt').toString().trim().split('\n');

input = input.map(item => item.split(' ').map(Number));

let answer = 0;
const [v, e] = input[0];
const edges = input.slice(1).sort((a, b) => a[2] - b[2]);
const unf = Array.from({ length: v + 1 }, (_, i) => i);

const Find = v => {
    if (v === unf[v]) return v;
    else return (unf[v] = Find(unf[v]));
};
const Union = (a, b) => {
    let fa = Find(a);
    let fb = Find(b);
    if (fa !== fb) unf[fa] = fb;
};

for (let i = 0; i < edges.length; i++) {
    if (Find(edges[i][0]) === Find(edges[i][1])) continue;
    Union(edges[i][0], edges[i][1]);
    answer += edges[i][2];
}

console.log(answer);
