// 11	43203007	14	marshal1101	314848	1952	node.js 	1666

const input = require('fs').readFileSync(
	'./test.txt'
).toString().trim().split('\n');

function exeQueue(input) {
    const N = +input[0];
    const data = [];
    let result = '';
    let frontPtr = 0;
    let backPtr = 0;

    for (let i = 1; i <= N; i++) {
        const order = input[i];

        switch (order) {
            case "pop" :
                if (frontPtr == backPtr) {
                    result += `${-1}\n`;
                } else {
                    result += `${data[frontPtr++]}\n`;
                }
                break;
            case "size" :
                if (frontPtr == backPtr) {
                    result += `${0}\n`;
                } else {
                    result += `${backPtr - frontPtr}\n`;
                }
                break;
            case "empty" :
                if (frontPtr == backPtr) {
                    result += `${1}\n`;
                } else {
                    result += `${0}\n`;
                }
                break;
            case "front" :
                if (frontPtr >= backPtr) {
                    result += `${-1}\n`;
                } else {
                    result += `${data[frontPtr]}\n`;
                }
                break;
            case "back" :
                if (backPtr <= frontPtr) {
                    result += `${-1}\n`;
                } else {
                    result += `${data[backPtr-1]}\n`;
                }
                break;
            default :
                const value = input[i].split(' ')[1];
                data[backPtr++] = value;
                break;
        }
    }

    return result;
}

console.log(exeQueue(input));