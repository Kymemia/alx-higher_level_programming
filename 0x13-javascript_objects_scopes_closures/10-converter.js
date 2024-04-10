#!/usr/bin/node
exports.converter = function (base) {
  return (number) => {
    return (function convert(num, fp) {
      return num === 0
        ? fp
        : convert(
            Math.floor(num / base),
            (base === 16 && num % base > 9)
              ? String.fromCharCode(num % base + 55) + fp
              : num % base + fp
	);
    })(number, '');
  };
};
