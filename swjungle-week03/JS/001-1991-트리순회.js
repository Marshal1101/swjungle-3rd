// 44	43390337	2	marshal1101	9344	124	node.js 	1211

const input = require('fs').readFileSync(
    'test.txt'   
).toString().trim().split('\n')

class Node {
    constructor(key, leftChild, rightChild) {
        this.key = key
        this.left = leftChild;
        this.right = rightChild;
    }
}

function preOrder(node) {
    let res = '';
    res += node.key;
    if (node.left !== '.') res += preOrder(tree[node.left]);
    if (node.right !== '.') res += preOrder(tree[node.right]);
    return res;
}

function inOrder(node) {
    let res = '';
    if (node.left !== '.') res += inOrder(tree[node.left]);
    res += node.key;
    if (node.right !== '.') res += inOrder(tree[node.right]);
    return res;
}

function postOrder(node) {
    let res = '';
    if (node.left !== '.') res += postOrder(tree[node.left]);
    if (node.right !== '.') res += postOrder(tree[node.right]);
    res += node.key;
    return res;
}

const N = +input.shift();
const tree = {};
input.forEach((line) => {
    const [node, left, right] = line.split(' ');
    tree[node] = new Node(node, left, right);
});

let result = '';
result += preOrder(tree['A'], result) + '\n';
result += inOrder(tree['A'], result) + '\n';
result += postOrder(tree['A'], result);

console.log(result);