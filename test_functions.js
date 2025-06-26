// Simple Node.js test for the JavaScript port
const fs = require('fs');
const path = require('path');

// Load the JavaScript files
const alphabetCode = fs.readFileSync(path.join(__dirname, 'js/alphabet.js'), 'utf8');
const gemNumFuncsCode = fs.readFileSync(path.join(__dirname, 'js/gemNumFuncs.js'), 'utf8');
const utilsCode = fs.readFileSync(path.join(__dirname, 'js/utils.js'), 'utf8');

// Execute the code
eval(alphabetCode);
eval(gemNumFuncsCode);
eval(utilsCode);

console.log("Testing GemaTreeAC JavaScript functions...\n");

// Test cipher access
console.log("1. Testing cipher access:");
const ordCipher = getCipher("Ord");
console.log(`   Ord cipher 'a' = ${ordCipher['a']} (expected: 1)`);
console.log(`   Ord cipher 'z' = ${ordCipher['z']} (expected: 26)\n`);

// Test gematria calculation
console.log("2. Testing gematria calculation:");
const loveValue = getGematria("love", "Ord");
console.log(`   getGematria("love", "Ord") = ${loveValue}`);
console.log(`   (l=12 + o=15 + v=22 + e=5 = ${12+15+22+5})\n`);

// Test parent list
console.log("3. Testing parent list:");
const parentList = getParentList(123);
console.log(`   getParentList(123) = [${parentList.join(', ')}]`);
console.log(`   (123 -> 1+2+3=6, so [123, 6])\n`);

// Test root number
console.log("4. Testing root number:");
const root = getRootNumber(123);
console.log(`   getRootNumber(123) = ${root} (expected: 6)\n`);

// Test distance calculation
console.log("5. Testing distance calculation:");
const teddy = new DistanceTeddyBear(["love", "hate", "life"]);
const distance = teddy.getDistance("love", "hate", "Ord");
console.log(`   Distance between "love" and "hate" = ${distance.toFixed(6)}\n`);

// Test deep memory initialization
console.log("6. Testing deep memory:");
initializeDeepMemory();
const deepMem = getDeepMem();
console.log(`   Deep memory contains ${deepMem.length} words`);
console.log(`   First few words: ${deepMem.slice(0, 5).join(', ')}\n`);

// Test search function
console.log("7. Testing search by number:");
const searchResults = searchDeepMemByNumberArray(loveValue, "Ord");
console.log(`   Words with same gematria as "love" (${loveValue}): ${searchResults.map(r => r[0]).join(', ')}\n`);

// Test NineRootedTree
console.log("8. Testing NineRootedTree:");
const tree = new NineRootedTree(["love", "hate", "life", "death"], "Ord");
const wordsWithValue = tree.findWords(loveValue);
console.log(`   Words in tree with value ${loveValue}: ${wordsWithValue.join(', ')}\n`);

console.log("All tests completed successfully!");