// Test the JavaScript modules functionality
const fs = require('fs');

// Mock the window object for Node.js testing
global.window = {
    GemaTreeAC: {}
};

// Load the modules
eval(fs.readFileSync('js/alphabet.js', 'utf8'));
eval(fs.readFileSync('js/gemNumFuncs.js', 'utf8'));
eval(fs.readFileSync('js/getwordsfromdbs.js', 'utf8'));
eval(fs.readFileSync('js/ndigitsets3.js', 'utf8'));

console.log('Testing GemaTreeAC JavaScript modules...\n');

// Test 1: getCipher function
console.log('Test 1: getCipher function');
const cipher = window.GemaTreeAC.getCipher('ScaExt');
console.log('ScaExt cipher loaded:', cipher && cipher['a'] === 1 ? 'PASS' : 'FAIL');
console.log('Value of "a" in ScaExt:', cipher['a']);

// Test 2: getGematria function
console.log('\nTest 2: getGematria function');
const gemValue = window.GemaTreeAC.getGematria('hello', 'ScaExt');
console.log(`getGematria('hello', 'ScaExt') = ${gemValue}`);
console.log('Type check:', typeof gemValue === 'number' ? 'PASS' : 'FAIL');

// Test 3: getRootNumber function
console.log('\nTest 3: getRootNumber function');
const root123 = window.GemaTreeAC.getRootNumber(123);
console.log(`getRootNumber(123) = ${root123} (expected: 6)`);
console.log('Result check:', root123 === 6 ? 'PASS' : 'FAIL');

// Test 4: getParentList function
console.log('\nTest 4: getParentList function');
const parents = window.GemaTreeAC.getParentList(123);
console.log(`getParentList(123) = [${parents.join(', ')}]`);
console.log('Type check:', Array.isArray(parents) ? 'PASS' : 'FAIL');
console.log('First element check:', parents[0] === 123 ? 'PASS' : 'FAIL');

// Test 5: Deep memory functions
console.log('\nTest 5: Deep memory functions');
const deepMem = window.GemaTreeAC.getDeepMem();
console.log('getDeepMem() type:', Array.isArray(deepMem) ? 'PASS' : 'FAIL');
console.log('Deep memory word count:', deepMem.length);

// Test 6: ndigitsets functions
console.log('\nTest 6: ndigitsets functions');
window.GemaTreeAC.clearRAM();
window.GemaTreeAC.addWord('test', 'ScaExt');
const treeOutput = window.GemaTreeAC.printAll('ScaExt');
console.log('printAll() type:', typeof treeOutput === 'string' ? 'PASS' : 'FAIL');
console.log('Tree output length:', treeOutput.length);

// Test 7: Multiple cipher calculations
console.log('\nTest 7: Multiple cipher calculations');
const ciphers = ['ScaExt', 'Ord', 'FullR'];
const testWord = 'gematria';
ciphers.forEach(cipherName => {
    const value = window.GemaTreeAC.getGematria(testWord, cipherName);
    console.log(`${testWord} in ${cipherName}: ${value}`);
});

console.log('\nAll tests completed!');