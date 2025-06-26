/**
 * Core gematria calculation functions - JavaScript port of gemNumFuncs.py
 */

/**
 * Calculate the gematria value of a word using the specified cipher
 * @param {string} word - The word to calculate
 * @param {string} currentCipher - The cipher to use
 * @returns {number} The gematria value
 */
function getGematria(word, currentCipher) {
    let number = 0;
    const cipherInUse = getCipher(currentCipher);
    
    for (const char of word) {
        number += cipherInUse[char] || 0;
    }
    
    return number;
}

/**
 * Get the n-digit set range for a given number of digits
 * @param {number} nDigits - Number of digits
 * @returns {Array} Array of numbers in the n-digit set
 */
function getNDS(nDigits) {
    const highestNumberInNDS = parseInt("9".repeat(nDigits));
    const lowestNumberInNDS = parseInt(Math.pow(10, nDigits - 1));
    
    const result = [];
    for (let i = lowestNumberInNDS; i <= highestNumberInNDS; i++) {
        result.push(i);
    }
    return result;
}

/**
 * Calculate the digital root (parent) of a number
 * @param {number} number - The number to process
 * @returns {number} The digital root
 */
function findParent(number) {
    const vstr = number.toString();
    let outVal = 0;
    
    for (const digit of vstr) {
        outVal += parseInt(digit);
    }
    
    return outVal;
}

/**
 * Get the complete path from a number to its root
 * @param {number} number - The starting number
 * @returns {Array} Array containing the complete path to root
 */
function getParentList(number) {
    const parList = [number];
    let parInt = number;
    
    while (parInt > 9) {
        parInt = findParent(parInt);
        parList.push(parInt);
    }
    
    return parList;
}

/**
 * Get the final root number (single digit)
 * @param {number} number - The number to process
 * @returns {number} The root number (1-9)
 */
function getRootNumber(number) {
    while (number > 9) {
        number = findParent(number);
    }
    return number;
}

/**
 * Get numbers in the same n-digit set that have the same root
 * @param {number} number - The reference number
 * @param {number} ndigitset - The n-digit set size
 * @returns {Array} Array of numbers with common root in the same n-digit set
 */
function getNWCPFromNDS(number, ndigitset) {
    const nds = getNDS(ndigitset);
    const outSet = [];
    const rootNum = getRootNumber(number);
    
    for (const num of nds) {
        if (getRootNumber(num) === rootNum) {
            outSet.push(num);
        }
    }
    
    return outSet;
}

/**
 * Get unique gematria values from a word-value tuple list
 * @param {Array} wordList - Array of [word, value] tuples
 * @returns {Array} Array of unique gematria values
 */
function getUniqueGematriaValuesInWVTupleList(wordList) {
    const outList = [];
    
    for (const item of wordList) {
        const gemval = item[1];
        if (!outList.includes(gemval)) {
            outList.push(gemval);
        }
    }
    
    return outList;
}

/**
 * Distance measurement class for calculating numerological relationships
 */
function DistanceTeddyBear(wordList) {
    this.wordList = wordList;
    this.pointBias = 0.01;
    this.distanceBias = 1.0;
    this.commonNds = 0.0;
    this.commonRoot = 0.0;
    this.commonRoute = 1.0;
    this.commonNumber = 0.0;
    this.sameWord = 0.0;
    this.closenessWeight = 1.0;
    this.numberDistanceWeight = 0.0;
    this.rootDistanceWeight = 0.0;
    this.ndsDistanceWeight = 0.0;
    this.maxDistance = 3.0;
}

DistanceTeddyBear.prototype.toString = function() {
    let selfString = "";
    selfString += "Point Bias: " + this.pointBias + " parameter pointBias\n";
    selfString += "Distance Bias: " + this.distanceBias + " parameter distanceBias\n";
    selfString += "Points from having a common nds: " + this.commonNds + " parameter commonNds\n";
    selfString += "Points from having a common root: " + this.commonRoot + " parameter commonRoot\n";
    selfString += "Points from having a common route: " + this.commonRoute + " parameter commonRoute\n";
    selfString += "Points from having a common number: " + this.commonNumber + " parameter commonNumber\n";
    selfString += "Points from being the same word: " + this.sameWord + " parameter sameWord\n";
    selfString += "Weight on points (how much points matter): " + this.closenessWeight + " parameter closenessWeight\n";
    selfString += "Weight on distance measure of numbers: " + this.numberDistanceWeight + " parameter numberDistanceWeight\n";
    selfString += "Weight on distance measure of roots: " + this.rootDistanceWeight + " parameter rootDistanceWeight\n";
    selfString += "Weight on distance measure of n-digit sets: " + this.ndsDistanceWeight + " parameter ndsDistanceWeight\n";
    selfString += "Maximum distance threshold: " + this.maxDistance + " parameter maxDistance\n\n";

    selfString += `
        The distance is calculated with:
            totalPoints = closenessWeight*(commonNds + commonRoot + commonRoute + commonNumber + sameWord)
            numberDistance = numberDistanceWeight*(abs(gematria(word1) - gematria(word2))
            rootDistance = rootDistanceWeight*(abs(root(word1) - root(word2)))
            ndsDistance = ndsDistanceWeight*(abs(nds(word1) - nds(word2)))

            distance = numberDistance + rootDistance + ndsDistance + distanceBias / totalPoints + pointBias
    `;
    
    return selfString;
};

/**
 * Calculate distance between two words
 * @param {string} word1 - First word
 * @param {string} word2 - Second word
 * @param {string} currentCipher - Cipher to use
 * @returns {number} Distance measure
 */
DistanceTeddyBear.prototype.getDistance = function(word1, word2, currentCipher) {
    const number01 = getGematria(word1, currentCipher);
    const number02 = getGematria(word2, currentCipher);
    const root01 = getRootNumber(number01);
    const root02 = getRootNumber(number02);
    const route01 = getParentList(number01).slice(1);
    const route02 = getParentList(number02).slice(1);
    const nds01 = number01.toString().length;
    const nds02 = number02.toString().length;

    let points = 0; // inverse measure of distance

    // Common n-digit set
    if (nds01 === nds02) {
        points += this.commonNds;
    }

    // Common root
    if (root01 === root02) {
        points += this.commonRoot;
    }

    // Common route
    if (JSON.stringify(route01) === JSON.stringify(route02)) {
        points += this.commonRoute;
    }

    // Common number
    if (number01 === number02) {
        points += this.commonNumber;
    }

    // Same word
    if (word1 === word2) {
        points += this.sameWord;
    }

    // Distance measures
    const numberDistance = this.numberDistanceWeight * Math.abs(number01 - number02);
    const rootDistance = this.rootDistanceWeight * Math.abs(root01 - root02);
    const ndsDistance = this.ndsDistanceWeight * Math.abs(nds01 - nds02);

    const totalPoints = this.closenessWeight * points;
    const distance = numberDistance + rootDistance + ndsDistance + 
                    this.distanceBias / (totalPoints + this.pointBias);

    return distance;
};

/**
 * Get a restricted word set based on distance criteria
 * @param {string} word - Reference word
 * @param {string} currentCipher - Cipher to use
 * @returns {Array} Array of [word, gematria, distance] tuples
 */
DistanceTeddyBear.prototype.getRestrictedWordSet_wdxy = function(word, currentCipher) {
    const outputArray = [];
    
    for (const dbWord of this.wordList) {
        const distance = this.getDistance(word, dbWord, currentCipher);
        if (distance < this.maxDistance && dbWord !== word) {
            outputArray.push([
                dbWord, 
                getGematria(dbWord, currentCipher), 
                distance
            ]);
        }
    }
    
    return outputArray;
};

/**
 * Get gematria values and distances in restricted word set
 * @param {string} word - Reference word
 * @param {string} currentCipher - Cipher to use
 * @returns {Array} Array of [gematria_value, distance] tuples
 */
DistanceTeddyBear.prototype.getGemValsAndDistancesInRWS = function(word, currentCipher) {
    const rws = this.getRestrictedWordSet_wdxy(word, currentCipher);
    const gwdArray = [];
    const chkUniqueArray = [];
    const uniqueGemvals = getUniqueGematriaValuesInWVTupleList(rws);
    
    for (const item of rws) {
        for (const gemval of uniqueGemvals) {
            if (item[1] === gemval) {
                if (!chkUniqueArray.includes(gemval)) {
                    chkUniqueArray.push(gemval);
                    gwdArray.push([gemval, this.getDistance(item[0], word, currentCipher)]);
                }
            }
        }
    }
    
    return gwdArray;
};