#!/usr/bin/node
exports.converter = function (base) {
  return function BaseConvert (number) {
    if (number === 0) {
      return '';
    } else {
      let rem = number % base;
      if (base === 16 && rem > 9) {
        rem = String.fromCharCode(rem + 87);
      }
      return BaseConvert(Math.floor(number / base)) + rem;
    }
  };
};
