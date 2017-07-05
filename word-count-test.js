const expect = require('chai').expect;

describe("words()", () => {
  it("counts one word", () => {
    let expectedCounts = { word: 1 };
    expect(words("word")).to.deep.equal(expectedCounts);
  });

  it("counts one of each", () => {
    let expectedCounts = { one: 1, of: 1, each: 1 };
    expect(words("one of each")).to.deep.equal(expectedCounts);
  });

  it("counts multiple occurrences", () => {
    let expectedCounts = { one: 1, fish: 4, two: 1, red: 1, blue: 1 };
    expect(words("one fish two fish red fish blue fish")).to.deep.equal(expectedCounts);
  });
});