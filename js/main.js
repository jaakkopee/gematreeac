/**
 * Main application logic for GemaTreeAC 2=0
 * Ported from PyScript blocks in GemaTreeAC_index.html
 */

// Global variables
let loadInfo = false;
let menuActive = false;
let deepMemWordTree = null;
let deepMemSyllableTree = null;
let sessionMemoryWordTree = null;
let sessionMemorySyllableTree = null;
let hwMenuControl = {};

// Simplified syllable tokenizer (alternative to NLTK)
function syllableTokenize(word) {
    // Simple syllable breaking based on vowel patterns
    // This is a basic implementation - in production you might want a more sophisticated tokenizer
    const vowels = 'aeiouåäöüøæëêéèïîíôóòõúûñàáâãčšž';
    const syllables = [];
    let currentSyllable = '';
    
    for (let i = 0; i < word.length; i++) {
        currentSyllable += word[i];
        
        if (vowels.includes(word[i].toLowerCase())) {
            // Look ahead to see if we should break here
            if (i < word.length - 1) {
                const nextChar = word[i + 1];
                if (!vowels.includes(nextChar.toLowerCase())) {
                    // Add consonant to current syllable if it's the only one
                    if (i < word.length - 2 && !vowels.includes(word[i + 2].toLowerCase())) {
                        currentSyllable += nextChar;
                        i++;
                    }
                    syllables.push(currentSyllable);
                    currentSyllable = '';
                }
            }
        }
    }
    
    if (currentSyllable) {
        syllables.push(currentSyllable);
    }
    
    return syllables.length > 0 ? syllables : [word];
}

/**
 * Extract syllables from word list
 * @param {Array} wordList - Array of words
 * @returns {Array} Array of syllable arrays
 */
function extractSyllables(wordList) {
    const outArray = [];
    for (let i = 0; i < wordList.length; i++) {
        outArray.push(syllableTokenize(wordList[i]));
    }
    return outArray;
}

/**
 * Change load mode - toggle between loading state and calculation
 */
function changeLoadMode() {
    console.log("changeLoadMode");
    if (!loadInfo) {
        loadInfo = true;
        document.getElementById("messageout").innerHTML = "Loading... please wait.";
        return;
    }
    loadInfo = false;
    const inputValue = document.getElementById("wordsHere").value;
    const currentCipher = localStorage.getItem("cipher");
    document.getElementById("messageout").innerHTML = window.GemaTreeAC.getGematria(inputValue, currentCipher);
}

/**
 * Change cipher and update UI
 * @param {Event} mE - Mouse event
 */
function changeCipher(mE) {
    localStorage.setItem("cipher", mE.currentTarget.cipherID);
    document.getElementById('cipherButton').innerHTML = "Cipher In Use: " + localStorage.getItem("cipher");
    
    initTrees(); // experimental
    
    clearWizard();
    clearSentenceFormulaNoMouse();
    smNoAddWordNoMouseNoChange();
    updateGemValMsgNotMouse();
}

/**
 * Toggle dropdown menu
 * @param {Event} mE - Mouse event
 */
function toggleMenu(mE) {
    if (!menuActive) {
        document.getElementById("ddc").style.display = "block";
        menuActive = true;
    } else {
        document.getElementById("ddc").style.display = "none";
        menuActive = false;
    }
}

/**
 * Toggle DMS parameters display
 * @param {Event} event - Click event
 */
function toggleDMSP(event) {
    const dmspDiv = document.getElementById("dmsSettings");
    if (dmspDiv.style.display !== "block") {
        dmspDiv.style.display = "block";
    } else {
        dmspDiv.style.display = "none";
    }
}

/**
 * Change DMS parameter and store in localStorage
 * @param {Event} evt - Change event
 */
function changeDMSParameter(evt) {
    const inputId = evt.currentTarget.inputId;
    localStorage.setItem("teddy_" + inputId, document.getElementById(inputId).valueAsNumber);
    console.log(inputId + " " + document.getElementById(inputId).valueAsNumber);
}

/**
 * RGB color callback for message animation
 */
function rgbCallBack01() {
    const red = Math.floor(Math.random() * 256);
    const green = Math.floor(Math.random() * 256);
    const blue = Math.floor(Math.random() * 256);
    document.getElementById("messageout").style.color = `rgb(${red}, ${green}, ${blue})`;
}

/**
 * Initialize final sentence
 */
function initFS() {
    const sentenceFormula = localStorage.getItem("sentenceFormula").split();
    let newFsIdxStr = "";
    for (let i = 0; i < sentenceFormula.length; i++) {
        newFsIdxStr += "0 ";
    }
    localStorage.setItem("finalSentenceIdx", newFsIdxStr);
}

/**
 * Get word value pairs from localStorage
 * @returns {Array} Array of [word, gematria_value] pairs
 */
function getWordValuePairsOuter() {
    const data = localStorage.getItem("words").split();
    const outdata = [];
    for (let i = 0; i < data.length; i++) {
        const word = data[i];
        const number = window.GemaTreeAC.getGematria(data[i], localStorage.getItem("cipher"));
        outdata.push([word, number]);
    }
    return outdata;
}

/**
 * Print wizard's comments for a given number
 * @param {Event} mE - Mouse event with datum property
 */
function printWizardsComments(mE) {
    const pressedNumber = parseInt(mE.currentTarget.datum);
    const pl = window.GemaTreeAC.getParentList(pressedNumber);
    let wvpairsFromDeepMemFormattedPL = "";

    for (let i = 0; i < pl.length; i++) {
        const wvpairsFromDeepMem = window.GemaTreeAC.searchDeepMemByNumberArray(pl[i], localStorage.getItem("cipher"));
        let wvpairsFromDeepMemFormatted = "";

        for (let j = 0; j < wvpairsFromDeepMem.length; j++) {
            const hyperWord = window.GemaTreeAC.makeWCHyperWord(wvpairsFromDeepMem[j][0]);
            wvpairsFromDeepMemFormatted += hyperWord + " " + wvpairsFromDeepMem[j][1] + "\n";
        }

        wvpairsFromDeepMemFormattedPL += wvpairsFromDeepMemFormatted;
    }

    let ldb_outputStr = "";
    const ldb_printed = [];
    const currentCipher = localStorage.getItem("cipher");

    if (localStorage.getItem("wizardsHelper")) {
        const wizardsHelperData = localStorage.getItem("wizardsHelper").split();

        for (let i = 0; i < wizardsHelperData.length; i++) {
            if (window.GemaTreeAC.getGematria(wizardsHelperData[i], currentCipher) === pressedNumber) {
                if (!ldb_printed.includes(wizardsHelperData[i])) {
                    ldb_outputStr += window.GemaTreeAC.makeLocDBHyperWord(wizardsHelperData[i]) + window.GemaTreeAC.getGematria(wizardsHelperData[i], currentCipher);
                    ldb_printed.push(wizardsHelperData[i]);
                }
            }
        }
    }

    const smviewDOC = document.getElementById('smview').contentWindow.document;
    smviewDOC.getElementById("WizardsComments").innerHTML = "Wizard Meditation on Route " + JSON.stringify(pl) + 
        "\n(Wizard's DeepMem-database from\nkotus-sanalista_v1,\nWordNet 3.1,\nGothenburg uni. Saldo 2.3\nand Väestötietojärjestelmän Etunimitilasto)\n\n" + 
        wvpairsFromDeepMemFormattedPL;
    smviewDOC.getElementById("WizardsHelper").innerHTML = "Local DB:\n" + ldb_outputStr;
    smviewDOC.location = "./sessionmemory.html#WChdr";

    // Set up listeners for the newly created elements
    for (let i = 0; i < pl.length; i++) {
        const wvpairsFromDeepMem = window.GemaTreeAC.searchDeepMemByNumberArray(pl[i], currentCipher);
        for (let j = 0; j < wvpairsFromDeepMem.length; j++) {
            makeWCListener(wvpairsFromDeepMem[j][0]);
        }
    }

    if (ldb_printed.length > 0) {
        for (let i = 0; i < ldb_printed.length; i++) {
            makeLocDBListener(ldb_printed[i]);
        }
    }
}

/**
 * Move word from deep memory to session words
 * @param {Event} mE - Mouse event
 */
function moveWordFromDMtoSW(mE) {
    const pressedWord = mE.currentTarget.sana;
    
    window.GemaTreeAC.clearRAM();
    const words = localStorage.getItem("words");
    const new_words = words + " " + pressedWord + " ";

    const oldWordArray = words.split();
    if (!oldWordArray.includes(pressedWord)) {
        localStorage.setItem("words", new_words);
    }
    
    outputWords();
    makeSWListeners();
    upDateSentenceFormulaNoChange();
    
    const smviewDOC = document.getElementById('smview').contentWindow.document;
    smviewDOC.location = "./sessionmemory.html#number" + window.GemaTreeAC.getGematria(pressedWord, localStorage.getItem("cipher"));
}

/**
 * Clear wizard display
 */
function clearWizard() {
    const smviewDOC = document.getElementById('smview').contentWindow.document;
    smviewDOC.getElementById("WizardsComments").innerHTML = "";
    smviewDOC.getElementById("WizardsHelper").innerHTML = "";
    smviewDOC.getElementById("dmSearchOutput").innerHTML = "";

    if (smviewDOC.getElementById("dmSearchPlot").src !== "") {
        const dmsDOC = smviewDOC.getElementById("dmSearchPlot").contentWindow.document;
        dmsDOC.getElementById("dmsLegendDiv").innerHTML = "";
        dmsDOC.getElementById("dmsDiv").innerHTML = "";
    }
}

/**
 * Output words to session memory view
 */
function outputWords() {
    window.GemaTreeAC.clearRAM();
    window.GemaTreeAC.addWordArray(localStorage.getItem("words").split(), localStorage.getItem("cipher"));

    const gtRepre = window.GemaTreeAC.printAll(localStorage.getItem("cipher"));
    
    const smviewDOC = document.getElementById('smview').contentWindow.document;
    smviewDOC.getElementById("smview_output").innerHTML = gtRepre;
}

/**
 * Get input string gematria value
 * @param {string} inputString - Input string
 * @returns {number} Gematria value
 */
function getInputStringGemValue(inputString) {
    inputString = inputString.toLowerCase();
    const inputArray = inputString.split();
    let outputString = "";
    for (let i = 0; i < inputArray.length; i++) {
        for (let j = 0; j < inputArray[i].length; j++) {
            if (/[a-zA-ZåäöüøæëêéèïîíôóòõúûñàáâãčšžÅÄÖÜØÆËÊÉÈÏÎÍÔÓÒÕÚÛÑÀÁÂÃČŠŽ]/.test(inputArray[i][j])) {
                outputString += inputArray[i][j];
            }
        }
    }
    return window.GemaTreeAC.getGematria(outputString, localStorage.getItem("cipher"));
}

/**
 * Update gematria value message
 * @param {Event} iE - Input event
 */
function updateGemValMsg(iE) {
    const inputString = document.getElementById("wordsHere").value;
    const output = document.getElementById("messageout");
    output.innerHTML = getInputStringGemValue(inputString);
}

/**
 * Update gematria value message without mouse event
 */
function updateGemValMsgNotMouse() {
    const inputString = document.getElementById("wordsHere").value;
    const output = document.getElementById("messageout");
    output.innerHTML = getInputStringGemValue(inputString);
}

/**
 * Initialize trees (NineRootedTree functionality)
 */
function initTrees() {
    console.log("initTrees()");

    const dmTreeWordList = window.GemaTreeAC.getDeepMem();
    console.log("deepMem words fetched.");
    const dmTreeSyllableList1D = window.GemaTreeAC.getDeepMemSyllables();
    console.log("deepMem syllables fetched.");

    const smTreeWordList = localStorage.getItem("words").split();
    const smTreeSyllableList2D = extractSyllables(smTreeWordList);
    const smTreeSyllableList1D = [];

    for (let i = 0; i < smTreeSyllableList2D.length; i++) {
        for (let j = 0; j < smTreeSyllableList2D[i].length; j++) {
            smTreeSyllableList1D.push(smTreeSyllableList2D[i][j]);
        }
    }

    console.log("Tree initialization complete");
    // Note: Actual NineRootedTree class implementation would go here
    // For now, we're using the simplified structure
}

/**
 * Add words with Enter key
 */
function smAddWordWithEnter() {
    window.GemaTreeAC.clearRAM();
    const new_words = document.getElementById("wordsHere").value.split();

    for (let wordIdx = 0; wordIdx < new_words.length; wordIdx++) {
        let word = new_words[wordIdx];
        const oldWordsStr = localStorage.getItem("words");
        word = word.toLowerCase();

        // Remove non-alphabetic characters
        word = word.replace(/[^a-zA-ZåäöüøæëêéèïîíôóòõúûñàáâãčšžÅÄÖÜØÆËÊÉÈÏÎÍÔÓÒÕÚÛÑÀÁÂÃČŠŽ]/g, "");

        const oldWords = oldWordsStr.split();
        if (!oldWords.includes(word)) {
            localStorage.setItem("words", oldWordsStr + " " + word + " ");
        }
    }

    outputWords();
    makeSWListeners();
    upDateSentenceFormulaNoChange();
}

/**
 * Clear session memory
 */
function clearSessionMemory() {
    localStorage.setItem("words", "0 ");
    localStorage.setItem("sentenceFormula", "0 ");
    initFS();
    window.GemaTreeAC.clearRAM();
    window.GemaTreeAC.addWord("0", localStorage.getItem("cipher"));
    clearWizard();
    outputWords();
    makeSWListeners();
    upDateSentenceFormulaNoChange();
}

/**
 * Clear sentence formula
 */
function clearSentenceFormula() {
    localStorage.setItem("sentenceFormula", "0 ");
    initFS();
    upDateSentenceFormulaNoChange();
}

/**
 * Clear sentence formula without mouse event
 */
function clearSentenceFormulaNoMouse() {
    localStorage.setItem("sentenceFormula", "0 ");
    initFS();
    upDateSentenceFormulaNoChange();
}

/**
 * Update sentence formula without change
 */
function upDateSentenceFormulaNoChange() {
    const oldWordsStr = localStorage.getItem("words");
    const smviewDOC = document.getElementById('smview').contentWindow.document;
    const output = smviewDOC.getElementById("sentenceFormulaLair");
    const formula = localStorage.getItem("sentenceFormula");
    
    output.innerHTML = window.GemaTreeAC.makeHyperFormula(formula, oldWordsStr, localStorage.getItem("cipher"));
    
    updateFsIdx();
    makeFinalSentenceListeners();
    printFinalSentence();
}

/**
 * Update final sentence index
 */
function updateFsIdx() {
    let fsIdxStr = localStorage.getItem("finalSentenceIdx");
    fsIdxStr += " 0 ";
    localStorage.setItem("finalSentenceIdx", fsIdxStr);
}

/**
 * Print final sentence
 */
function printFinalSentence() {
    const smviewDOC = document.getElementById('smview').contentWindow.document;
    const output = smviewDOC.getElementById("finalSentenceLair");
    output.innerHTML = makeFinalSentence();
}

/**
 * Make final sentence from formula and indices
 * @returns {string} Final sentence string
 */
function makeFinalSentence() {
    const wordArray = window.GemaTreeAC.make2DWordArrayFromString(localStorage.getItem("words"), localStorage.getItem("cipher"));
    
    const fsFormulaStr = localStorage.getItem("sentenceFormula");
    const fsFormulaArray = fsFormulaStr.split();
    
    const fsIdxStr = localStorage.getItem("finalSentenceIdx");
    const fsIdxArray = fsIdxStr.split();

    let outputString = "";
    
    let fwc = 0;
    for (let i = 0; i < fsFormulaArray.length; i++) {
        for (let j = 0; j < wordArray.length; j++) {
            if (window.GemaTreeAC.getGematria(wordArray[j][0], localStorage.getItem("cipher")) === parseInt(fsFormulaArray[i])) {
                outputString += wordArray[j][parseInt(fsIdxArray[fwc])] + " ";
                fwc++;
                break;
            }
        }
    }

    return outputString;
}

/**
 * Make session word listeners
 */
function makeSWListeners() {
    // Implementation would set up event listeners for session word elements
    console.log("makeSWListeners() - placeholder implementation");
}

/**
 * Make final sentence listeners
 */
function makeFinalSentenceListeners() {
    // Implementation would set up event listeners for final sentence elements
    console.log("makeFinalSentenceListeners() - placeholder implementation");
}

/**
 * Make wizard comment listener
 * @param {string} word - Word to create listener for
 */
function makeWCListener(word) {
    // Implementation would set up event listener for wizard comment word
    console.log("makeWCListener() for word:", word);
}

/**
 * Make local database listener
 * @param {string} word - Word to create listener for
 */
function makeLocDBListener(word) {
    // Implementation would set up event listener for local database word
    console.log("makeLocDBListener() for word:", word);
}

/**
 * Perform actions that don't require mouse events
 */
function smNoAddWordNoMouseNoChange() {
    // Placeholder for complex session memory operations
    console.log("smNoAddWordNoMouseNoChange() - placeholder implementation");
}

/**
 * Delete words from input box
 */
function delWordsFromInputBox() {
    document.getElementById("wordsHere").value = "";
    updateGemValMsgNotMouse();
}

/**
 * Add words when Enter key is pressed
 * @param {KeyboardEvent} kP - Keyboard event
 */
function addWordsWithEnter(kP) {
    if (kP.key === "Enter") {
        smAddWordWithEnter();
    }
}

/**
 * Initialize page functionality
 */
function initializePage() {
    console.log("Initializing GemaTreeAC JavaScript version...");

    // Initialize localStorage defaults
    if (!localStorage.getItem("cipher")) {
        localStorage.setItem("cipher", "ScaExt");
    }

    document.getElementById('cipherButton').innerHTML = "Cipher In Use: " + localStorage.getItem("cipher");

    if (!localStorage.getItem("words")) {
        localStorage.setItem("words", "0 ");
    }

    if (!localStorage.getItem("sentenceFormula")) {
        localStorage.setItem("sentenceFormula", "0 ");
    }

    if (!localStorage.getItem("finalSentenceIdx")) {
        initFS();
    }

    // Set up cipher button event listeners
    const cipherProxy = changeCipher;

    const cipherButtons = [
        { id: "ccscaext", cipherID: "ScaExt" },
        { id: "ccengextrev", cipherID: "EngExtRev" },
        { id: "ccord", cipherID: "Ord" },
        { id: "ccordrev", cipherID: "OrdRev" },
        { id: "ccfr", cipherID: "FullR" },
        { id: "ccfrrev", cipherID: "FullRRev" },
        { id: "ccsr", cipherID: "SingRed" },
        { id: "ccsrrev", cipherID: "SingRedRev" },
        { id: "ccfibo", cipherID: "Fibonacci" },
        { id: "ccfiborev", cipherID: "FibonacciRev" }
    ];

    cipherButtons.forEach(button => {
        const element = document.getElementById(button.id);
        if (element) {
            element.cipherID = button.cipherID;
            element.addEventListener("click", cipherProxy);
        }
    });

    // Set up dropdown menu
    const ddButton = document.getElementById("cipherButton");
    ddButton.addEventListener("click", toggleMenu);

    // Set up DMS parameters
    const dmsParamsButton = document.getElementById("showDMSParams");
    dmsParamsButton.addEventListener("click", toggleDMSP);

    // Initialize DMS parameters from localStorage
    const dmsParams = [
        "pointBias", "distanceBias", "commonNds", "commonRoot", "commonRoute",
        "commonNumber", "sameWord", "closenessWeight", "numberDistanceWeight",
        "rootDistanceWeight", "ndsDistanceWeight", "maxDistance"
    ];

    const dmsDefaults = {
        pointBias: 0.001, distanceBias: 1.0, commonNds: 0.0, commonRoot: 1.0,
        commonRoute: 1.0, commonNumber: 0.0, sameWord: 0.0, closenessWeight: 1.0,
        numberDistanceWeight: 0.0001, rootDistanceWeight: 0.0, ndsDistanceWeight: 0.0,
        maxDistance: 10.0
    };

    dmsParams.forEach(param => {
        if (!localStorage.getItem("teddy_" + param)) {
            localStorage.setItem("teddy_" + param, dmsDefaults[param]);
        }
        const element = document.getElementById(param);
        if (element) {
            element.value = localStorage.getItem("teddy_" + param);
            element.addEventListener("change", changeDMSParameter);
            element.inputId = param;
        }
    });

    // Set up input field event listeners
    document.getElementById("wordsHere").addEventListener("click", delWordsFromInputBox);
    document.getElementById("wordsHere").addEventListener("keypress", addWordsWithEnter);
    document.getElementById("wordsHere").addEventListener("input", updateGemValMsg);

    // Set up button event listeners
    document.getElementById("addWordToSM").addEventListener("click", smAddWordWithEnter);
    document.getElementById("clearSM").addEventListener("click", clearSessionMemory);
    document.getElementById("clearSF").addEventListener("click", clearSentenceFormula);

    // Start RGB animation
    setInterval(rgbCallBack01, 333);

    // Initialize page state
    outputWords();
    makeSWListeners();
    upDateSentenceFormulaNoChange();
    updateGemValMsgNotMouse();

    // Initialize trees
    initTrees();

    console.log("GemaTreeAC JavaScript initialization complete!");
}

// Initialize when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializePage);
} else {
    initializePage();
}