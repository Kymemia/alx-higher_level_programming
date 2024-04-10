#!/usr/bin/node
exports.converter = function (base) {
  return function BaseConvert (number) {
    return (function convert(numm, fp) {
      return numm === 0
        ? fp
        : convert(Math.floor(numm / base), (base === 16 && numm % base > 9)
          ? String.fromCharCode(numm % base + 55) + fp
          : numm % base + fp);
    })(number, '');
  };
};
