#!/usr/bin/node
exports.converter = function (base) {
  return function BaseConvert (number) {
    if (number === 0) {
      return 0;
    } else {
      let fp = '';
      while (number > 0) {
        const remainder = number % base;
        if (base === 16 && remainder > 9) {
          fp = String.fromCharCode(remainder + 55) + fp;
        } else {
          fp = remainder + fp;
        }
        number = Math.floor(number / base);
      }
      return fp;
    }
  };
};
