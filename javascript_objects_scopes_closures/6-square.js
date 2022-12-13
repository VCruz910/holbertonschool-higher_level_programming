#!/usr/bin/node
const SquareP = require('./5-square');

class square extends SquareP {
    charPrint(C) {
        if (C === undefined) {
            C = 'X';
        }
        for (let I = 0; I < this.height; I++) {
            let S = '';
            for (let J = 0; J < this.width; J++) {
                S += C;
            }
            console.log(S);
        }
    }
}

module.exports = Square;