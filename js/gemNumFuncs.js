/**
 * Gematria Numerical Functions module
 * Ported from gemNumFuncs.py
 */

/**
 * Calculate gematria value of a word using specified cipher
 * @param {string} word - The word to calculate
 * @param {string} currentCipher - The cipher to use
 * @returns {number} The gematria value
 */
function getGematria(word, currentCipher) {
    let number = 0;
    const cipherInUse = window.GemaTreeAC.getCipher(currentCipher);
    for (let i = 0; i < word.length; i++) {
        number += cipherInUse[word[i]] || 0;
    }
    return number;
}

/**
 * Get n-digit set range
 * @param {number} nDigits - Number of digits
 * @returns {Array} Range of numbers in the n-digit set
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
 * Find parent of a number (sum of digits)
 * @param {number} number - The number to find parent of
 * @returns {number} Sum of digits
 */
function findParent(number) {
    const vstr = number.toString();
    let outVal = 0;
    for (let i = 0; i < vstr.length; i++) {
        outVal += parseInt(vstr[i]);
    }
    return outVal;
}

/**
 * Get list of parents from number to root
 * @param {number} number - The starting number
 * @returns {Array} List of numbers from original to root
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
 * Get root number (final single digit)
 * @param {number} number - The number to find root of
 * @returns {number} The root number (1-9)
 */
function getRootNumber(number) {
    while (number > 9) {
        number = findParent(number);
    }
    return number;
}

/**
 * Get unique gematria values from word-value tuple list
 * @param {Array} wordList - Array of [word, value] tuples
 * @returns {Array} Array of unique gematria values
 */
function getUniqueGematriaValuesInWVTupleList(wordList) {
    const outList = [];
    for (let i = 0; i < wordList.length; i++) {
        const gemval = wordList[i][1];
        if (!outList.includes(gemval)) {
            outList.push(gemval);
        }
    }
    return outList;
}

/**
 * Get numbers with common parents from n-digit set
 * @param {number} number - The reference number
 * @param {number} ndigitset - The n-digit set to search in
 * @returns {Array} Numbers with common root
 */
function getNWCPFromNDS(number, ndigitset) {
    const nds = getNDS(ndigitset);
    const outSet = [];
    for (let i = 0; i < nds.length; i++) {
        if (getRootNumber(number) === getRootNumber(nds[i])) {
            outSet.push(nds[i]);
        }
    }
    return outSet;
}

/**
 * Calculate basic distance between two words
 * @param {string} word1 - First word
 * @param {string} word2 - Second word
 * @param {string} currentCipher - Cipher to use
 * @param {number} closenessWeight - Weight for closeness (default 1.0)
 * @returns {number} Distance measure
 */
function getDistance(word1, word2, currentCipher, closenessWeight = 1.0) {
    const number01 = getGematria(word1, currentCipher);
    const number02 = getGematria(word2, currentCipher);
    const root01 = getRootNumber(number01);
    const root02 = getRootNumber(number02);
    const route01 = getParentList(number01).slice(1);
    const route02 = getParentList(number02).slice(1);
    let points = 0.01; // inverse measure of distance

    // common n digit set
    if (number01.toString().length === number02.toString().length) {
        points += 0.01;
    }

    // common root
    if (root01 === root02) {
        points += 0.02;
    }

    // common route
    if (JSON.stringify(route01) === JSON.stringify(route02)) {
        points += 0.08;
    }

    // common number
    if (number01 === number02) {
        points += 0.16;
    }

    // same word
    if (word1 === word2) {
        points += 0.061;
    }

    // distance measures
    const numberDistance = 0.06 * Math.abs(number01 - number02);
    const rootDistance = 0.6 * Math.abs(root01 - root02);
    const totalDistance = (rootDistance + numberDistance) / (points * closenessWeight);

    return totalDistance;
}

/**
 * Distance measurement class for advanced gematria analysis
 */
class DistanceTeddyBear {
    constructor(wordList) {
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

    toString() {
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
    }

    getDistance(word1, word2, currentCipher) {
        const number01 = getGematria(word1, currentCipher);
        const number02 = getGematria(word2, currentCipher);
        const root01 = getRootNumber(number01);
        const root02 = getRootNumber(number02);
        const route01 = getParentList(number01).slice(1);
        const route02 = getParentList(number02).slice(1);
        const nds01 = number01.toString().length;
        const nds02 = number02.toString().length;
        
        let points = 0; // inverse measure of distance

        // common n digit set
        if (nds01 === nds02) {
            points += this.commonNds;
        }

        // common root
        if (root01 === root02) {
            points += this.commonRoot;
        }

        // common route
        if (JSON.stringify(route01) === JSON.stringify(route02)) {
            points += this.commonRoute;
        }

        // common number
        if (number01 === number02) {
            points += this.commonNumber;
        }

        // same word
        if (word1 === word2) {
            points += this.sameWord;
        }

        // distance measures
        const numberDistance = this.numberDistanceWeight * Math.abs(number01 - number02);
        const rootDistance = this.rootDistanceWeight * Math.abs(root01 - root02);
        const ndsDistance = this.ndsDistanceWeight * Math.abs(nds01 - nds02);

        const totalDistance = (rootDistance + numberDistance + ndsDistance + this.distanceBias) / 
                             ((points * this.closenessWeight) + this.pointBias);

        return totalDistance;
    }

    getRestrictedWordSet(word, currentCipher) {
        const outputArray = [];
        for (let i = 0; i < this.wordList.length; i++) {
            const distance = this.getDistance(word, this.wordList[i], currentCipher);
            if (distance < this.maxDistance) {
                outputArray.push([this.wordList[i], getGematria(this.wordList[i], currentCipher)]);
            }
        }
        return outputArray;
    }

    getRestrictedWordSet_wd(word, currentCipher) {
        const outputArray = [];
        for (let i = 0; i < this.wordList.length; i++) {
            const distance = this.getDistance(word, this.wordList[i], currentCipher);
            if (distance < this.maxDistance) {
                outputArray.push([this.wordList[i], getGematria(this.wordList[i], currentCipher), distance]);
            }
        }
        return outputArray;
    }

    getRestrictedWordSet_wdxy(word, currentCipher) {
        const outputArray = [];
        const dataSetForXY = [];
        
        for (let i = 0; i < this.wordList.length; i++) {
            const distance = this.getDistance(word, this.wordList[i], currentCipher);
            const gemVal = getGematria(this.wordList[i], currentCipher);
            if (distance < this.maxDistance) {
                outputArray.push([this.wordList[i], gemVal, distance, 0, 0]);
                if (!dataSetForXY.includes(gemVal)) {
                    dataSetForXY.push(gemVal);
                }
            }
        }

        let highestNumberInDataSet = 0.0;
        for (let i = 0; i < dataSetForXY.length; i++) {
            if (dataSetForXY[i] > highestNumberInDataSet) {
                highestNumberInDataSet = dataSetForXY[i];
            }
        }

        for (let i = 0; i < outputArray.length; i++) {
            const angle = (outputArray[i][1] / highestNumberInDataSet) * 360.0;
            const x = Math.sin(angle) * outputArray[i][2];
            const y = Math.cos(angle) * outputArray[i][2];

            outputArray[i][3] = x;
            outputArray[i][4] = y;
        }

        return outputArray;
    }

    getGemValsAndDistancesInRWS(word, currentCipher) {
        const rws = this.getRestrictedWordSet(word, currentCipher);
        const gwdArray = [];
        const chkUniqueArray = [];
        const uniqueGemvals = getUniqueGematriaValuesInWVTupleList(rws);
        
        for (let i = 0; i < rws.length; i++) {
            for (let j = 0; j < uniqueGemvals.length; j++) {
                if (rws[i][1] === uniqueGemvals[j]) {
                    if (!chkUniqueArray.includes(uniqueGemvals[j])) {
                        chkUniqueArray.push(uniqueGemvals[j]);
                        gwdArray.push([uniqueGemvals[j], this.getDistance(rws[i][0], word, currentCipher)]);
                    }
                }
            }
        }
        
        return gwdArray;
    }
}

// Export for both module and global usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        getGematria,
        getNDS,
        findParent,
        getParentList,
        getRootNumber,
        getUniqueGematriaValuesInWVTupleList,
        getNWCPFromNDS,
        getDistance,
        DistanceTeddyBear
    };
} else {
    window.GemaTreeAC = window.GemaTreeAC || {};
    Object.assign(window.GemaTreeAC, {
        getGematria,
        getNDS,
        findParent,
        getParentList,
        getRootNumber,
        getUniqueGematriaValuesInWVTupleList,
        getNWCPFromNDS,
        getDistance,
        DistanceTeddyBear
    });
}