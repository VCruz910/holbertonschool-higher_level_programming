#!/usr/bin/node
exports.callMeMoby = function (number, theFunction) {
  theFunction.call(this, number + 1);
};
