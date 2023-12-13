const fs = require("fs");
const { start } = require("repl");

const specialCharacterPattern = /[!@#$%^&*()_+\-=\[\]{};':"\\|,<>\/?]/;

function loadFile(filePath) {
  try {
    const data = fs.readFileSync(filePath, "utf8");
    return data;
  } catch (err) {
    console.error(`Error reading file from disk: ${err}`);
  }
}

const findNumbersInRow = (row) => {
  const matches = [];
  row.replace(/\d+/g, (match, offset) => {
    matches.push({
      number: Number(match),
      startIndex: offset,
      endIndex: offset + match.length - 1,
    });
  });
  return matches;
};

const isEnginePartNumber = (rowNumbers, rows) => {
  const { row, matches } = rowNumbers;
  const numbers = [];
  matches.forEach((match) => {
    const { number, startIndex, endIndex } = match;
    //left
    if (
      startIndex > 0 &&
      specialCharacterPattern.test(rows[row][startIndex - 1])
    ) {
      numbers.push(number);
      return;
    }
    //right
    if (
      endIndex < rows[row].length &&
      specialCharacterPattern.test(rows[row][endIndex + 1])
    ) {
      numbers.push(number);
      return;
    }
    //top
    if (row > 0) {
      const topRow = row - 1;
      for (let i = startIndex; i <= endIndex; i++) {
        if (specialCharacterPattern.test(rows[topRow][i])) {
          numbers.push(number);
          return;
        }
      }
      //left top corner & top right corner
      if (
        startIndex != 0 &&
        specialCharacterPattern.test(rows[topRow][startIndex - 1])
      ) {
        numbers.push(number);
        return;
      }
      if (
        endIndex != rows[topRow].length &&
        specialCharacterPattern.test(rows[topRow][endIndex + 1])
      ) {
        numbers.push(number);
        return;
      }
    }

    if (row < rows.length - 1) {
      const bottomRow = row + 1;
      for (let i = startIndex; i <= endIndex; i++) {
        if (specialCharacterPattern.test(rows[bottomRow][i])) {
          numbers.push(number);
          return;
        }
      }
      //left bottom corner & bottom right corner
      if (
        startIndex != 0 &&
        specialCharacterPattern.test(rows[bottomRow][startIndex - 1])
      ) {
        numbers.push(number);
        return;
      }
      if (
        endIndex != rows[bottomRow].length &&
        specialCharacterPattern.test(rows[bottomRow][endIndex + 1])
      ) {
        numbers.push(number);
        return;
      }
    }
  });
  //console.log(row, numbers);
  return numbers;
};

const task = (input) => {
  const test = loadFile(input);
  const rows = test.split("\n");
  const numbers = [];
  rows.forEach((row, index) => {
    numbers.push({ matches: findNumbersInRow(row), row: index });
  });

  //! OK console.log("Numbers", numbers.map(n => n.matches))

  const properNumbers = numbers.map((rowNumbers) => {
    return isEnginePartNumber(rowNumbers, rows);
  });

  //console.log('Proper numbers', properNumbers)

  const sum = properNumbers.flat().reduce((a, b) => a + b, 0);

  console.log(sum);
  return sum;
};

//! test
const test = task("./input_test.txt");
const properTask = task("./input.txt");
