#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let I = 0; I < list.length; I++) {
    if (searchElement === list[I]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
