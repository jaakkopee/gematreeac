/**
 * Database and utility functions - JavaScript port of getwordsfromdbs.py and other utilities
 */

// Simple in-memory database replacement for deep memory words
let deepMemoryWords = [];
let deepMemorySyllables = [];

/**
 * Initialize deep memory with some default words (simplified version)
 * In the original, this would load from SQLite database
 */
function initializeDeepMemory() {
    // Basic English words for demonstration
    deepMemoryWords = [
        "love", "hate", "life", "death", "light", "dark", "good", "evil", "truth", "lie",
        "hope", "fear", "joy", "pain", "peace", "war", "strong", "weak", "big", "small",
        "hot", "cold", "fast", "slow", "young", "old", "new", "old", "high", "low",
        "right", "wrong", "yes", "no", "up", "down", "in", "out", "on", "off"
    ];
    
    // Basic syllables
    deepMemorySyllables = [
        "a", "an", "and", "the", "is", "it", "to", "of", "in", "for", "on", "with",
        "as", "by", "at", "be", "or", "not", "are", "from", "you", "all", "but", "can"
    ];
}

/**
 * Get the deep memory word list
 * @returns {Array} Array of words
 */
function getDeepMem() {
    if (deepMemoryWords.length === 0) {
        initializeDeepMemory();
    }
    return deepMemoryWords;
}

/**
 * Get the deep memory syllables list
 * @returns {Array} Array of syllables
 */
function getDeepMemSyllables() {
    if (deepMemorySyllables.length === 0) {
        initializeDeepMemory();
    }
    return deepMemorySyllables;
}

/**
 * Search deep memory by gematria number
 * @param {number} number - The gematria value to search for
 * @param {string} currentCipher - The cipher to use
 * @returns {Array} Array of [word, gematria] tuples
 */
function searchDeepMemByNumberArray(number, currentCipher) {
    const results = [];
    const words = getDeepMem();
    
    for (const word of words) {
        const gemVal = getGematria(word, currentCipher);
        if (gemVal === number) {
            results.push([word, gemVal]);
        }
    }
    
    return results;
}

/**
 * Simple syllable tokenizer (basic implementation)
 * @param {string} word - Word to tokenize
 * @returns {Array} Array of syllables
 */
function tokenizeSyllables(word) {
    // Very basic syllable splitting - count vowel groups
    const vowels = 'aeiouAEIOU';
    const syllables = [];
    let currentSyllable = '';
    let lastWasVowel = false;
    
    for (let i = 0; i < word.length; i++) {
        const char = word[i];
        const isVowel = vowels.includes(char);
        
        if (isVowel && !lastWasVowel && currentSyllable.length > 0) {
            syllables.push(currentSyllable);
            currentSyllable = char;
        } else {
            currentSyllable += char;
        }
        
        lastWasVowel = isVowel;
    }
    
    if (currentSyllable.length > 0) {
        syllables.push(currentSyllable);
    }
    
    return syllables.length > 0 ? syllables : [word];
}

/**
 * Extract syllables from word list
 * @param {Array} wordList - Array of words
 * @returns {Array} 2D array of syllables
 */
function extractSyllables(wordList) {
    const outArray = [];
    for (const word of wordList) {
        outArray.push(tokenizeSyllables(word));
    }
    return outArray;
}

/**
 * Create a 2D word array with gematria values
 * @param {Array} words - Array of words  
 * @param {string} currentCipher - Cipher to use
 * @returns {Array} 2D array where each sub-array contains words with same gematria
 */
function make2DWordArray(words, currentCipher) {
    const wordGroups = {};
    
    for (const word of words) {
        const gemVal = getGematria(word, currentCipher);
        if (!wordGroups[gemVal]) {
            wordGroups[gemVal] = [];
        }
        if (!wordGroups[gemVal].includes(word)) {
            wordGroups[gemVal].push(word);
        }
    }
    
    return Object.values(wordGroups);
}

/**
 * Create a 2D word array from a string
 * @param {string} wordsString - Space-separated words
 * @param {string} currentCipher - Cipher to use
 * @returns {Array} 2D array grouped by gematria value
 */
function make2DWordArrayFromString(wordsString, currentCipher) {
    const words = wordsString.split(/\s+/).filter(word => word.length > 0);
    return make2DWordArray(words, currentCipher);
}

/**
 * Generate a random number between min and max (inclusive)
 * @param {number} min - Minimum value
 * @param {number} max - Maximum value
 * @returns {number} Random number
 */
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Get a random choice from an array
 * @param {Array} array - Array to choose from
 * @returns {*} Random element
 */
function randomChoice(array) {
    if (array.length === 0) return null;
    return array[Math.floor(Math.random() * array.length)];
}

/**
 * Create hyperlink HTML for words (simplified version of ndigitsets3.py functions)
 * @param {string} word - Word to make into hyperlink
 * @returns {string} HTML string
 */
function makeWCHyperWord(word) {
    return `<button id="WC${word}" class="WC_style">${word}</button> `;
}

/**
 * Create hyperlink HTML for local database words
 * @param {string} word - Word to make into hyperlink
 * @returns {string} HTML string
 */
function makeLocDBHyperWord(word) {
    return `<button id="LDB${word}" class="LocDB_style">${word}</button> `;
}

/**
 * Create hyperlink HTML for distance measure search results
 * @param {Array} searchResults - Array of search result tuples
 * @param {number} searchedGemVal - The gematria value that was searched
 * @param {string} currentCipher - Current cipher
 * @returns {string} HTML string
 */
function makeDMSHyperRepre(searchResults, searchedGemVal, currentCipher) {
    let output = `<h3>Distance Measure Search Results for ${searchedGemVal}:</h3>\n`;
    
    for (const result of searchResults) {
        const [word, gemVal, distance] = result;
        output += `<button id="dmsButton${word}" class="dmsButton">${word}</button> `;
        output += `(${gemVal}, dist: ${distance.toFixed(3)})<br>\n`;
    }
    
    return output;
}

/**
 * Simple NineRootedTree class (simplified version)
 */
function NineRootedTree(wordList, currentCipher) {
    this.wordList = wordList;
    this.currentCipher = currentCipher;
    this.roots = {};
    
    // Group words by root number
    for (const word of wordList) {
        const gemVal = getGematria(word, currentCipher);
        const root = getRootNumber(gemVal);
        
        if (!this.roots[root]) {
            this.roots[root] = [];
        }
        if (!this.roots[root].includes(word)) {
            this.roots[root].push(word);
        }
    }
}

/**
 * Find words with a specific gematria value
 * @param {number} gematria - The gematria value to search for
 * @returns {Array} Array of words
 */
NineRootedTree.prototype.findWords = function(gematria) {
    const results = [];
    for (const word of this.wordList) {
        if (getGematria(word, this.currentCipher) === gematria) {
            results.push(word);
        }
    }
    return results;
};