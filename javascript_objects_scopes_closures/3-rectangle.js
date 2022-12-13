#!/usr/bin/node
class Rectangle {
  constructor (W_Rec, H_Rec) {
    if ((W_Rec > 0) && (H_Rec > 0)) {
      this.width = W_Rec;
      this.height = H_Rec;
    }
  }

  print () {
    for (let I = 0; I < this.height; I++) {
      let S = '';
      for (let J = 0; J < this.width; J++) {
        S += 'X';
      }
      console.log(S);
    }
  }
}

module.exports = Rectangle;
