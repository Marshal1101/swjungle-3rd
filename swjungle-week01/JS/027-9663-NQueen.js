const fs = require('fs');
let input = fs.readFileSync('/home/chilling4u/Marshal1101/swjungle-3rd-s1-algorithm/swjungle-week01/JS/test.txt').toString().trim();

function soulution(N) {
    const iPos = Array(N).fill(0);
    const flagIpos = Array(N).fill(0);
    const flagRightUp = Array(2*N-1).fill(0);
    const flagRightDown = Array(2*N-1).fill(0);
    let count = 0;

    function nQueen(N, i) {
        for (let j = 0; j < N; j++) {
            if (!flagIpos[j] && !flagRightUp[i+j] && !flagRightDown[i-j+N-1]) {
                iPos[i] = j;
                if (i === N-1) {
                    count += 1;
                }
                else {
                    flagIpos[j] = flagRightUp[i+j] = flagRightDown[i-j+N-1] = true;
                    nQueen(N, i + 1);
                    flagIpos[j] = flagRightUp[i+j] = flagRightDown[i-j+N-1] = false;
                }
            }
        }
    }
    
    nQueen(N, 0);
    console.log(count);
}

soulution(Number(input));