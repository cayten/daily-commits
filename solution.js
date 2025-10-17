
function solve(input) {
  // Çözümünü buraya yaz. input string gelir; çıktı string dön.
  const nums = input.trim().split(/\s+/).map(x => parseInt(x, 10)).filter(n => !Number.isNaN(n));
  return String(nums.reduce((a,b)=>a+b,0));
}

if (require.main === module) {
  const fs = require('fs');
  const data = fs.readFileSync(0, 'utf8');
  console.log(solve(data));
}

module.exports = { solve };
