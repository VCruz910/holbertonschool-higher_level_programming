#!/usr/bin/node
class Rectangle {
    constructor(W_Rec, H_Rec) {
        if ((W_Rec > 0) && (H_Rec > 0)) {
            this.width = W_Rec;
            this.height = H_Rec;
        }
    }
}

module.exports = Rectangle;