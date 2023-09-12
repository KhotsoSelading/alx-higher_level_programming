#!/usr/bin/node
// a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, element) {
  return list.filter(x => x === element).length;
};
