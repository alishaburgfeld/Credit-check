var cc = require("./creditCheck");

test("should validate credit card", () => {
  expect(cc.creditCheck("5541808923795240")).toBe("The number is valid!");
  expect(cc.creditCheck("4024007136512380")).toBe("The number is valid!");
  expect(cc.creditCheck("6011797668867828")).toBe("The number is valid!");

  expect(cc.creditCheck("5541801923795240")).toBe("The number is invalid!");
  expect(cc.creditCheck("4024007106512380")).toBe("The number is invalid!");
  expect(cc.creditCheck("6011797668868728")).toBe("The number is invalid!");
});
