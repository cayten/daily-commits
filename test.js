
const { solve } = require('./solution');

function assertEqual(a, b, msg) {
  if (a !== b) {
    throw new Error(msg + ` | got=${a} expected=${b}`);
  }
}

(function run() {
  assertEqual(solve("1 2 3\n"), "6", "sum basic");
  assertEqual(solve("10 -2 5"), "13", "sum with negative");
  console.log("OK");
})();
