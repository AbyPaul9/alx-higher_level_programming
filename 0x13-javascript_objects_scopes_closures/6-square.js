#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (prmCharacter) {
    if (prmCharacter === undefined) {
      this.print();
    } else {
      for (let row = 0; row < this.height; row++) {
        for (let column = 0; column < this.width; column++) {
          process.stdout.write(prmCharacter);
        }
        process.stdout.write('\n');
      }
    }
  }
};
