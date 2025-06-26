/**
 * Database functions module
 * Ported from getwordsfromdbs.py with client-side adaptations
 */

// In-memory word database (simplified version of DeepMem)
// This would ideally be loaded from a JSON file or IndexedDB in a real implementation
let deepMemWords = [
    // Sample words for testing - in production this would be loaded from external source
    "word", "test", "hello", "world", "gematria", "numerology", "tree", "root", "cipher",
    "calculation", "algorithm", "distance", "search", "database", "memory", "session",
    "formula", "sentence", "wizard", "comments", "helper", "local", "deep", "restricted"
];

let deepMemSyllables = [
    // Sample syllables for testing
    "word", "test", "hel", "lo", "wor", "ld", "ge", "ma", "tri", "a", "nu", "mer", "ol", "o", "gy"
];

/**
 * Search word list by distance measure
 * @param {string} word - Search word
 * @param {Array} wordList - List of words to search
 * @param {string} currentCipher - Cipher to use
 * @param {number} closenessWeight - Closeness weight (default 1.0)
 * @param {number} maxDistance - Maximum distance threshold (default 1.0)
 * @returns {Array} Array of [word, gematria_value] tuples
 */
function searchWordListByDistance(word, wordList, currentCipher, closenessWeight = 1.0, maxDistance = 1.0) {
    const outputArray = [];
    for (let i = 0; i < wordList.length; i++) {
        const distance = window.GemaTreeAC.getDistance(word, wordList[i], currentCipher, closenessWeight);
        if (distance < maxDistance && !outputArray.some(item => item[0] === wordList[i])) {
            outputArray.push([wordList[i], window.GemaTreeAC.getGematria(wordList[i], currentCipher)]);
        }
    }
    return outputArray;
}

/**
 * Get deep memory words
 * @returns {Array} Array of words from deep memory
 */
function getDeepMem() {
    return [...deepMemWords]; // Return copy to avoid modification
}

/**
 * Get deep memory syllables
 * @returns {Array} Array of syllables from deep memory
 */
function getDeepMemSyllables() {
    return [...deepMemSyllables]; // Return copy to avoid modification
}

/**
 * Search deep memory by distance measure
 * @param {string} word - Search word
 * @param {string} currentCipher - Cipher to use
 * @param {number} closenessWeight - Closeness weight (default 1.0)
 * @param {number} maxDistance - Maximum distance threshold (default 1.0)
 * @returns {Array} Array of [word, gematria_value] tuples
 */
function searchDeepMemByDistance(word, currentCipher, closenessWeight = 1.0, maxDistance = 1.0) {
    const outputArray = [];
    for (let i = 0; i < deepMemWords.length; i++) {
        const distance = window.GemaTreeAC.getDistance(word, deepMemWords[i], currentCipher, closenessWeight);
        if (distance < maxDistance && !outputArray.some(item => item[0] === deepMemWords[i])) {
            outputArray.push([deepMemWords[i], window.GemaTreeAC.getGematria(deepMemWords[i], currentCipher)]);
        }
    }
    return outputArray;
}

/**
 * Search deep memory by number array (gematria values)
 * @param {number} number - Gematria value to search for
 * @param {string} currentCipher - Cipher to use
 * @returns {Array} Array of [word, gematria_value] tuples matching the number
 */
function searchDeepMemByNumberArray(number, currentCipher) {
    const outputArray = [];
    for (let i = 0; i < deepMemWords.length; i++) {
        const gemVal = window.GemaTreeAC.getGematria(deepMemWords[i], currentCipher);
        if (gemVal === number) {
            outputArray.push([deepMemWords[i], gemVal]);
        }
    }
    return outputArray;
}

/**
 * Load deep memory from external source (JSON file, API, etc.)
 * This function can be extended to load data from various sources
 * @param {string} source - Source URL or data
 * @returns {Promise} Promise resolving to loaded data
 */
async function loadDeepMemFromSource(source) {
    try {
        if (typeof source === 'string' && source.startsWith('http')) {
            // Load from URL
            const response = await fetch(source);
            const data = await response.json();
            if (data.words) deepMemWords = data.words;
            if (data.syllables) deepMemSyllables = data.syllables;
            return { words: deepMemWords, syllables: deepMemSyllables };
        } else if (typeof source === 'object') {
            // Load from object
            if (source.words) deepMemWords = source.words;
            if (source.syllables) deepMemSyllables = source.syllables;
            return { words: deepMemWords, syllables: deepMemSyllables };
        }
    } catch (error) {
        console.error('Error loading deep memory:', error);
        return null;
    }
}

/**
 * Add words to deep memory
 * @param {Array} words - Array of words to add
 */
function addWordsToDeepMem(words) {
    for (let i = 0; i < words.length; i++) {
        if (!deepMemWords.includes(words[i])) {
            deepMemWords.push(words[i]);
        }
    }
}

/**
 * Add syllables to deep memory
 * @param {Array} syllables - Array of syllables to add
 */
function addSyllablesToDeepMem(syllables) {
    for (let i = 0; i < syllables.length; i++) {
        if (!deepMemSyllables.includes(syllables[i])) {
            deepMemSyllables.push(syllables[i]);
        }
    }
}

/**
 * Clear deep memory
 */
function clearDeepMem() {
    deepMemWords = [];
    deepMemSyllables = [];
}

/**
 * Get statistics about deep memory
 * @returns {Object} Object with statistics
 */
function getDeepMemStats() {
    return {
        wordCount: deepMemWords.length,
        syllableCount: deepMemSyllables.length,
        totalItems: deepMemWords.length + deepMemSyllables.length
    };
}

// Export for both module and global usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        searchWordListByDistance,
        getDeepMem,
        getDeepMemSyllables,
        searchDeepMemByDistance,
        searchDeepMemByNumberArray,
        loadDeepMemFromSource,
        addWordsToDeepMem,
        addSyllablesToDeepMem,
        clearDeepMem,
        getDeepMemStats
    };
} else {
    window.GemaTreeAC = window.GemaTreeAC || {};
    Object.assign(window.GemaTreeAC, {
        searchWordListByDistance,
        getDeepMem,
        getDeepMemSyllables,
        searchDeepMemByDistance,
        searchDeepMemByNumberArray,
        loadDeepMemFromSource,
        addWordsToDeepMem,
        addSyllablesToDeepMem,
        clearDeepMem,
        getDeepMemStats
    });
}