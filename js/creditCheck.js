
/**
 * This function checks if the credit card number is valid.
 *
 * @param {String} string The credit card number to validate
 */
const creditCheck = (string) => {
  const reversed = Array.from(string).reverse().map(digit => parseInt(digit));

  const result = [];

  for (let i = 0; i < reversed.length ; i++) {
    if (i % 2 == 1) {
      const newDigit = reversed[i] * 2;

      if (newDigit < 10) {
        result.push(newDigit);
      } else {
        let digitSum = 0;

        for (const digit of Array.from(newDigit.toString()).map(digit => parseInt(digit))) {
          digitSum += digit;
        }

        result.push(digitSum)
      }
    } else {
      result.push(reversed[i])
    }
  }

  const resultSum = result.reduce((acc, curr) => acc + curr, 0);

  return (resultSum % 10 === 0) ? "The number is valid!" : "The number is invalid!"; 
};

module.exports = { creditCheck };
