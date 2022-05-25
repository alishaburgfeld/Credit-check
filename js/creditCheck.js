/**
 * This function returns the sum of the digits in a number.
 *
 * @param {Number} num The number to sum the digits of
 * @returns {Number} The sum of the digits of the number
 */
const digitSum = (num) => {
  return Array.from(num.toString()).reduce(
    (sum, digit) => sum + parseInt(digit),
    0
  );
};

/**
 * This function checks if the credit card number is valid.
 *
 * @param {String} string The credit card number to validate
 */
const creditCheck = (string) => {
  nums = Array.from(string).map((digit) => parseInt(digit));

  for (let i = nums.length - 2; i >= 0; i -= 2) {
    nums[i] *= 2;
    if (nums[i] > 9) {
      nums[i] = digitSum(nums[i]);
    }
  }

  return digitSum(nums.join("")) % 10 === 0 ? "The number is valid!" : "The number is invalid!";
};

module.exports = { creditCheck };
