#!/usr/bin/node
exports.converter = function (base) {
  return function BaseConvert (number) {
    if (number === 0) {
      return '';
    } else {
      if (base === 16 && number % base > 9) {
        return BaseConvert(Math.floor(number / base)) + String.fromCharCode(number % base + 87);
      }
      return BaseConvert(Math.floor(number / base)) + number % base;
    }
  };
};
