/**
 * N-Digit Sets module - Nine-rooted tree data structure
 * Ported from ndigitsets3.py
 */

/**
 * Root class for organizing words by their numerological root
 */
class Root {
    constructor(word, currentCipher) {
        let chkWord = word;
        const alphakeys = Object.keys(window.GemaTreeAC.getCipher(currentCipher));
        
        for (let i = 0; i < chkWord.length; i++) {
            if (!alphakeys.includes(chkWord[i])) {
                chkWord = chkWord.replace(chkWord[i], "0");
            }
        }

        const gemVal = window.GemaTreeAC.getGematria(chkWord, currentCipher);
        this.root = window.GemaTreeAC.getRootNumber(gemVal);
        this.words = [chkWord];
        this.routes = [window.GemaTreeAC.getParentList(gemVal).slice(1)];
        this.printed = [];
    }

    getWords() {
        return this.words;
    }

    addWord(word, currentCipher) {
        const gemVal = window.GemaTreeAC.getGematria(word, currentCipher);
        const route = window.GemaTreeAC.getParentList(gemVal).slice(1);
           
        if (this.root === window.GemaTreeAC.getRootNumber(gemVal)) {
            const routeExists = this.routes.some(r => JSON.stringify(r) === JSON.stringify(route));
            
            if (routeExists) {
                this.words.push(word);
                return true;
            }

            this.words.push(word);
            this.routes.push(route);
            return true;
        }
        
        return false;
    }

    makeHyperWord(word, currentCipher) {
        const words2D = make2DWordArray(this.words, currentCipher);
        let outputWord = "";

        for (let chkWordIdx = 0; chkWordIdx < words2D.length; chkWordIdx++) {
            const chkWord = words2D[chkWordIdx];
            if (window.GemaTreeAC.getGematria(chkWord[0], currentCipher) === window.GemaTreeAC.getGematria(word, currentCipher)) {
                
                const isAlreadyPrinted = this.printed.some(p => JSON.stringify(p) === JSON.stringify(chkWord));
                if (!isAlreadyPrinted) {
                    for (let i = 0; i < chkWord.length; i++) {
                        outputWord += 
                            `<div class='hyperWordDiv' id='hwd_${window.GemaTreeAC.getGematria(chkWord[i], currentCipher)}_${chkWord[i]}'>` +
                            `<button class='hyperWordButton' id='hwb_${chkWord[i]}'>${chkWord[i]}</button>` +
                            `<div class='hyperWordMenuContent' id='hwmc_${chkWord[i]}'>` +
                                `<a href='#smview_output' id='hwDel_${chkWord[i]}'>delete</a>` +
                                `<a href='#DMShdr' id='hwDiMe_${chkWord[i]}'>DMSearch</a>` +
                            `</div>` +
                            `</div>`;
                    }
                    
                    this.printed.push(chkWord);
                } else {
                    return "printed";
                }
            }
        }

        return outputWord;
    }

    printMe(currentCipher) {
        let retval = "";
        retval += 
            `<div class='Root' id='Root_${this.root}'>` +
                `<div class='rootClass' id='rootP_${this.root}'>` +
                    `Root ${this.root}</div>`;

        for (let routeIter of this.routes) {
            retval += `<br><div class='routeClass' id='route_${routeIter}'>Route ${JSON.stringify(routeIter)}</div>`;
            
            const wordsToBePrintedOnThisRoute = [];
            for (let word of this.words) {
                const wordRoute = window.GemaTreeAC.getParentList(window.GemaTreeAC.getGematria(word, currentCipher)).slice(1);
                if (JSON.stringify(wordRoute) === JSON.stringify(routeIter)) {
                    wordsToBePrintedOnThisRoute.push(word);
                }
            }
            
            let oldGemVal = 0;
            for (let word_idx = 0; word_idx < wordsToBePrintedOnThisRoute.length; word_idx++) {
                const gemVal = window.GemaTreeAC.getGematria(wordsToBePrintedOnThisRoute[word_idx], currentCipher);

                if (word_idx > 0) {
                    oldGemVal = window.GemaTreeAC.getGematria(wordsToBePrintedOnThisRoute[word_idx - 1], currentCipher);
                }
            
                if (gemVal !== oldGemVal || word_idx === 0) {
                    retval += makeHyperNumber(gemVal.toString());
                }
                    
                const hyperWord = this.makeHyperWord(wordsToBePrintedOnThisRoute[word_idx], currentCipher);

                if (hyperWord !== "printed") {
                    retval += hyperWord;
                }
            }
        }
        
        retval += "</div><br>";
        return retval;
    }

    sortWords(currentCipher) {
        for (let i = 1; i < this.words.length; i++) {
            const key = this.words[i];
            let j = i - 1;
            
            while (j >= 0 && window.GemaTreeAC.getGematria(key, currentCipher) < window.GemaTreeAC.getGematria(this.words[j], currentCipher)) {
                this.words[j + 1] = this.words[j];
                j--;
            }
            this.words[j + 1] = key;
        }
    }
}

/**
 * Create hyperlink number button
 * @param {string} numStr - Number as string
 * @returns {string} HTML string for hyperlink number
 */
function makeHyperNumber(numStr) {
    let newNumStr = "";
    if (numStr === "0") {
        newNumStr += 
            `<div class='hyperWordDiv' id='hwd_${numStr}_${numStr}'>` +
                `<button class='hyperNumberButton' id='hwb_nolla'>${numStr}</button>` +
                `<div class='hyperWordMenuContent' id='hwmc_${numStr}'>` +
                    `<a href='#WCHdr' id='hwWCSearch_${numStr}'>GemVal:${numStr}</a>` +
                    `<a href='#SentenceFormulaLair' id='hwSF_${numStr}'>SentForm:${numStr}</a>` +
                `</div>` +
            `</div>`;
    } else {
        newNumStr += 
            `<div class='hyperWordDiv' id='hwd_${numStr}_${numStr}'>` +
                `<button class='hyperNumberButton' id='hwb_${numStr}'>${numStr}</button>` +
                `<div class='hyperWordMenuContent' id='hwmc_${numStr}'>` +
                    `<a href='#WCHdr' id='hwWCSearch_${numStr}'>GemVal:${numStr}</a>` +
                    `<a href='#SentenceFormulaLair' id='hwSF_${numStr}'>SentForm:${numStr}</a>` +
                `</div>` +
            `</div>`;
    }

    return newNumStr;
}

/**
 * Create wizard comment hyperlink word
 * @param {string} word - The word
 * @returns {string} HTML string for wizard comment button
 */
function makeWCHyperWord(word) {
    return `<button id='WC${word}' value='${word}'>${word}</button>`;
}

/**
 * Create local database hyperlink word
 * @param {string} word - The word
 * @returns {string} HTML string for local database button
 */
function makeLocDBHyperWord(word) {
    return `<button id='LDB${word}' value='${word}'>${word}</button>`;
}

/**
 * Create hyperlink formula representation
 * @param {string} formula - Formula string
 * @param {string} wordListStr - Word list string
 * @param {string} currentCipher - Current cipher
 * @returns {string} HTML string for formula
 */
function makeHyperFormula(formula, wordListStr, currentCipher) {
    const wordArray2D = make2DWordArrayFromString(wordListStr, currentCipher);
    const formulaList = formula.split();
    const formulaOutArray = [];

    for (let i = 0; i < formulaList.length; i++) {
        for (let j = 0; j < wordArray2D.length; j++) {
            if (window.GemaTreeAC.getGematria(wordArray2D[j][0], currentCipher) === parseInt(formulaList[i])) {
                formulaOutArray.push(wordArray2D[j]);
            }
        }
    }

    let outputString = "";
    for (let i = 0; i < formulaOutArray.length; i++) {
        const parentList = window.GemaTreeAC.getParentList(window.GemaTreeAC.getGematria(formulaOutArray[i][0], currentCipher));
        outputString += `<button class='sfNumber'>${JSON.stringify(parentList)}</button>`;

        for (let j = 0; j < formulaOutArray[i].length; j++) {
            outputString += `<button class='sfString' id='SF${formulaOutArray[i][j]}'>${formulaOutArray[i][j]}</button> `;
        }

        outputString += "<br>";
    }

    return outputString;
}

/**
 * Create DMS (Distance Measure Search) hyperlink representation
 * @param {Array} inputArray - Input array with search results
 * @param {number} searchedGemVal - Searched gematria value
 * @param {string} currentCipher - Current cipher
 * @returns {string} HTML string for DMS representation
 */
function makeDMSHyperRepre(inputArray, searchedGemVal, currentCipher) {
    let outputString = "";
    
    const rootNumber = window.GemaTreeAC.getRootNumber(searchedGemVal);
    const routeToRoot = window.GemaTreeAC.getParentList(searchedGemVal).slice(1);

    for (let i = 0; i < inputArray.length; i++) {
        let colorRGB = "rgb(0,0,0)";
        
        if (inputArray[i][1].toString().length === searchedGemVal.toString().length) {
            colorRGB = "rgb(0,0,204)";
        }
        
        if (window.GemaTreeAC.getRootNumber(inputArray[i][1]) === rootNumber) {
            colorRGB = "rgb(0,204,204)";
        }

        const itemRoute = window.GemaTreeAC.getParentList(inputArray[i][1]).slice(1);
        if (JSON.stringify(itemRoute) === JSON.stringify(routeToRoot)) {
            colorRGB = "rgb(204,0,127)";
        }
        
        if (parseInt(inputArray[i][1]) === parseInt(searchedGemVal)) {
            colorRGB = "rgb(153,153,0)";
        }

        outputString += `<button class='dmsButton' id='dmsButton${inputArray[i][0]}' style='color:${colorRGB}' value='${inputArray[i][0]}'>${inputArray[i][0]}</button>${window.GemaTreeAC.getGematria(inputArray[i][0], currentCipher)}`;
    }

    return outputString;
}

/**
 * Create 2D word array from string
 * @param {string} wordString - Word string
 * @param {string} currentCipher - Current cipher
 * @returns {Array} 2D array of words grouped by gematria value
 */
function make2DWordArrayFromString(wordString, currentCipher) {
    const wordArrayFlat = wordString.split();
    const wordArray = [];
    
    for (let i = 0; i < wordArrayFlat.length; i++) {
        const tmpArray = [];

        for (let j = 0; j < wordArrayFlat.length; j++) {
            if (window.GemaTreeAC.getGematria(wordArrayFlat[i], currentCipher) === window.GemaTreeAC.getGematria(wordArrayFlat[j], currentCipher)) {
                if (!tmpArray.includes(wordArrayFlat[j])) {
                    tmpArray.push(wordArrayFlat[j]);
                }
            }
        }

        const isArrayInWordArray = wordArray.some(arr => JSON.stringify(arr) === JSON.stringify(tmpArray));
        if (!isArrayInWordArray) {
            wordArray.push(tmpArray);
        }
    }

    return wordArray;
}

/**
 * Create 2D word array from array
 * @param {Array} InWordArray - Input word array
 * @param {string} currentCipher - Current cipher
 * @returns {Array} 2D array of words grouped by gematria value
 */
function make2DWordArray(InWordArray, currentCipher) {
    const wordArrayFlat = InWordArray;
    const wordArray = [];
    
    for (let i = 0; i < wordArrayFlat.length; i++) {
        const tmpArray = [];

        for (let j = 0; j < wordArrayFlat.length; j++) {
            if (window.GemaTreeAC.getGematria(wordArrayFlat[i], currentCipher) === window.GemaTreeAC.getGematria(wordArrayFlat[j], currentCipher)) {
                if (!tmpArray.includes(wordArrayFlat[j])) {
                    tmpArray.push(wordArrayFlat[j]);
                }
            }
        }

        const isArrayInWordArray = wordArray.some(arr => JSON.stringify(arr) === JSON.stringify(tmpArray));
        if (!isArrayInWordArray) {
            wordArray.push(tmpArray);
        }
    }

    return wordArray;
}

// Global roots array
let roots = [];

/**
 * Sort roots by root number
 */
function sortRoots() {
    for (let i = 1; i < roots.length; i++) {
        const key = roots[i];
        let j = i - 1;
        
        while (j >= 0 && key.root < roots[j].root) {
            roots[j + 1] = roots[j];
            j--;
        }
        roots[j + 1] = key;
    }
}

/**
 * Sort words and roots
 * @param {string} currentCipher - Current cipher
 */
function sortWordsAndRoots(currentCipher) {
    for (let i = 0; i < roots.length; i++) {
        roots[i].sortWords(currentCipher);
    }
    sortRoots();
}

/**
 * Add word to roots structure
 * @param {string} word - Word to add
 * @param {string} currentCipher - Current cipher
 */
function addWord(word, currentCipher) {
    if (roots.length === 0) {
        roots.push(new Root(word, currentCipher));
        return;
    }

    let rootFound = false;
    for (let i = 0; i < roots.length; i++) {
        rootFound = roots[i].addWord(word, currentCipher);
        if (rootFound) {
            sortWordsAndRoots(currentCipher);
            return;
        }
    }

    if (!rootFound) {
        roots.push(new Root(word, currentCipher));
        sortWordsAndRoots(currentCipher);
    }
}

/**
 * Add array of words
 * @param {Array} wordArray - Array of words to add
 * @param {string} currentCipher - Current cipher
 */
function addWordArray(wordArray, currentCipher) {
    for (let i = 0; i < wordArray.length; i++) {
        addWord(wordArray[i], currentCipher);
    }
}

/**
 * Print all roots
 * @param {string} currentCipher - Current cipher
 * @returns {string} HTML representation of all roots
 */
function printAll(currentCipher) {
    let retval = "";
    
    for (let i = 0; i < roots.length; i++) {
        retval += roots[i].printMe(currentCipher);
    }

    return retval;
}

/**
 * Clear RAM - reset roots array
 */
function clearRAM() {
    roots = [];
}

// Export for both module and global usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        Root,
        makeHyperNumber,
        makeWCHyperWord,
        makeLocDBHyperWord,
        makeHyperFormula,
        makeDMSHyperRepre,
        make2DWordArrayFromString,
        make2DWordArray,
        sortRoots,
        sortWordsAndRoots,
        addWord,
        addWordArray,
        printAll,
        clearRAM
    };
} else {
    window.GemaTreeAC = window.GemaTreeAC || {};
    Object.assign(window.GemaTreeAC, {
        Root,
        makeHyperNumber,
        makeWCHyperWord,
        makeLocDBHyperWord,
        makeHyperFormula,
        makeDMSHyperRepre,
        make2DWordArrayFromString,
        make2DWordArray,
        sortRoots,
        sortWordsAndRoots,
        addWord,
        addWordArray,
        printAll,
        clearRAM
    });
}