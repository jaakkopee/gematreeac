/**
 * Gematria cipher definitions - JavaScript port of alphabet.py
 */

const cipher = {};

cipher["ScaExt"] = {
    "0": 0, "/": 0, "ã": 1, "á": 1, "â": 1, "à": 1, "a": 1, "b": 2, "ç": 3, "c": 3,
    "d": 4, "ë": 5, "ê": 5, "é": 5, "è": 5, "e": 5, "f": 6, "g": 7, "h": 8,
    "ï": 9, "î": 9, "í": 9, "i": 9, "j": 10, "k": 20, "l": 30, "m": 40,
    "ñ": 50, "n": 50, "ô": 60, "ó": 60, "ò": 60, "õ": 60, "o": 60, "þ": 70,
    "p": 70, "q": 80, "r": 90, "š": 100, "s": 100, "t": 200, "ú": 300,
    "û": 300, "u": 300, "v": 400, "w": 500, "x": 600, "ü": 700, "y": 700,
    "ž": 800, "z": 800, "å": 900, "æ": 1000, "ä": 1000, "ø": 2000, "ö": 2000
};

cipher["EngExtRev"] = {
    "0": 0, "/": 0, "ã": 800, "á": 800, "â": 800, "à": 800, "a": 800, "b": 700,
    "ç": 600, "c": 600, "d": 500, "ë": 400, "ê": 400, "é": 400, "è": 400,
    "e": 400, "f": 300, "g": 200, "h": 100, "ï": 90, "î": 90, "í": 90, "i": 90,
    "j": 80, "k": 70, "l": 60, "m": 50, "ñ": 40, "n": 40, "ô": 30, "ó": 30,
    "ò": 30, "õ": 30, "o": 30, "þ": 20, "p": 20, "q": 10, "r": 9, "š": 8,
    "s": 8, "t": 7, "ú": 6, "û": 6, "u": 6, "v": 5, "w": 4, "x": 3, "ü": 2,
    "y": 2, "ž": 1, "z": 1, "å": 800, "æ": 800, "ä": 800, "ø": 30, "ö": 30
};

cipher["Ord"] = {
    "0": 0, "/": 0, "ã": 1, "á": 1, "â": 1, "à": 1, "a": 1, "b": 2, "ç": 3,
    "c": 3, "4": 4, "d": 4, "ë": 5, "ê": 5, "é": 5, "è": 5, "e": 5, "f": 6,
    "g": 7, "h": 8, "ï": 9, "î": 9, "í": 9, "i": 9, "j": 10, "k": 11, "l": 12,
    "m": 13, "ñ": 14, "n": 14, "ô": 15, "ó": 15, "ò": 15, "õ": 15, "o": 15,
    "þ": 16, "p": 16, "q": 17, "r": 18, "š": 19, "s": 19, "t": 20, "ú": 21,
    "û": 21, "u": 21, "v": 22, "w": 23, "x": 24, "ü": 21, "y": 25, "ž": 26,
    "z": 26, "å": 1, "æ": 1, "ä": 1, "ø": 15, "ö": 15
};

cipher["OrdRev"] = {
    "0": 0, "/": 0, "ã": 26, "á": 26, "â": 26, "à": 26, "a": 26, "b": 25,
    "ç": 24, "c": 24, "d": 23, "ë": 22, "ê": 22, "é": 22, "è": 22, "e": 22,
    "f": 21, "g": 20, "h": 19, "ï": 18, "î": 18, "í": 18, "i": 18, "j": 17,
    "k": 16, "l": 15, "m": 14, "ñ": 13, "n": 13, "ô": 12, "ó": 12, "ò": 12,
    "õ": 12, "o": 12, "þ": 11, "p": 11, "q": 10, "r": 9, "š": 8, "s": 8,
    "t": 7, "ú": 6, "û": 6, "u": 6, "v": 5, "w": 4, "x": 3, "ü": 6, "y": 2,
    "ž": 1, "z": 1, "å": 26, "æ": 26, "ä": 26, "ø": 12, "ö": 12
};

cipher["FullR"] = {
    "0": 0, "/": 0, "ã": 1, "á": 1, "â": 1, "à": 1, "a": 1, "b": 2, "ç": 3,
    "c": 3, "4": 4, "d": 4, "ë": 5, "ê": 5, "é": 5, "è": 5, "e": 5, "f": 6,
    "g": 7, "h": 8, "ï": 9, "î": 9, "í": 9, "i": 9, "j": 1, "k": 2, "l": 3,
    "m": 4, "ñ": 5, "n": 5, "ô": 6, "ó": 6, "ò": 6, "õ": 6, "o": 6, "þ": 7,
    "p": 7, "q": 8, "r": 9, "š": 1, "s": 1, "t": 2, "ú": 3, "û": 3, "u": 3,
    "v": 4, "w": 5, "x": 6, "ü": 3, "y": 7, "ž": 8, "z": 8, "å": 1, "æ": 1,
    "ä": 1, "ø": 6, "ö": 6
};

cipher["FullRRev"] = {
    "0": 0, "/": 0, "ã": 8, "á": 8, "â": 8, "à": 8, "a": 8, "b": 7, "ç": 6,
    "c": 6, "d": 5, "ë": 4, "ê": 4, "é": 4, "è": 4, "e": 4, "f": 3, "g": 2,
    "h": 1, "ï": 9, "î": 9, "í": 9, "i": 9, "j": 8, "k": 7, "l": 6, "m": 5,
    "ñ": 4, "n": 4, "ô": 3, "ó": 3, "ò": 3, "õ": 3, "o": 3, "þ": 2, "p": 2,
    "q": 1, "r": 9, "š": 8, "s": 8, "t": 7, "ú": 6, "û": 6, "u": 6, "v": 5,
    "w": 4, "x": 3, "ü": 6, "y": 2, "ž": 1, "z": 1, "å": 8, "æ": 8, "ä": 8,
    "ø": 3, "ö": 3
};

cipher["SingRed"] = {
    "0": 0, "/": 0, "ã": 1, "á": 1, "â": 1, "à": 1, "a": 1, "b": 2, "ç": 3,
    "c": 3, "d": 4, "ë": 5, "ê": 5, "é": 5, "è": 5, "e": 5, "f": 6, "g": 7,
    "h": 8, "ï": 9, "î": 9, "í": 9, "i": 9, "j": 1, "k": 2, "l": 3, "m": 4,
    "ñ": 5, "n": 5, "ô": 6, "ó": 6, "ò": 6, "õ": 6, "o": 6, "þ": 7, "p": 7,
    "q": 8, "r": 9, "š": 10, "s": 10, "t": 2, "ú": 3, "û": 3, "u": 3, "v": 4,
    "w": 5, "x": 6, "ü": 7, "y": 7, "ž": 8, "z": 8, "å": 1, "æ": 1, "ä": 1,
    "ø": 6, "ö": 6
};

cipher["SingRedRev"] = {
    "0": 0, "/": 0, "ã": 8, "á": 8, "â": 8, "à": 8, "a": 8, "b": 7, "ç": 6,
    "c": 6, "d": 5, "ë": 4, "ê": 4, "é": 4, "è": 4, "e": 4, "f": 3, "g": 2,
    "h": 10, "ï": 9, "î": 9, "í": 9, "i": 9, "j": 8, "k": 7, "l": 6, "m": 5,
    "ñ": 4, "n": 4, "ô": 3, "ó": 3, "ò": 3, "õ": 3, "o": 3, "þ": 2, "p": 2,
    "q": 1, "r": 9, "š": 8, "s": 8, "t": 7, "ú": 6, "û": 6, "u": 6, "v": 5,
    "w": 4, "x": 3, "ü": 6, "y": 2, "ž": 1, "z": 1, "å": 8, "æ": 8, "ä": 8,
    "ø": 3, "ö": 3
};

cipher["Fibonacci"] = {
    "0": 0, "/": 0, "ã": 1, "á": 1, "â": 1, "à": 1, "a": 1, "b": 1, "ç": 2,
    "c": 2, "d": 3, "ë": 5, "ê": 5, "é": 5, "è": 5, "e": 5, "f": 8, "g": 13,
    "h": 21, "ï": 34, "î": 34, "í": 34, "i": 34, "j": 55, "k": 89, "l": 144,
    "m": 233, "ñ": 377, "n": 377, "ô": 610, "ó": 610, "ò": 610, "õ": 610,
    "o": 610, "þ": 987, "p": 987, "q": 1597, "r": 2584, "š": 4181, "s": 4181,
    "t": 6765, "ú": 10946, "û": 10946, "u": 10946, "v": 17711, "w": 28657,
    "x": 46368, "ü": 75025, "y": 75025, "ž": 121393, "z": 121393, "å": 1,
    "æ": 1, "ä": 1, "ø": 610, "ö": 610
};

cipher["FibonacciRev"] = {
    "0": 0, "/": 0, "ã": 121393, "á": 121393, "â": 121393, "à": 121393,
    "a": 121393, "b": 75025, "ç": 46368, "c": 46368, "d": 28657, "ë": 17711,
    "ê": 17711, "é": 17711, "è": 17711, "e": 17711, "f": 10946, "g": 6765,
    "h": 4181, "ï": 2584, "î": 2584, "í": 2584, "i": 2584, "j": 1597, "k": 987,
    "l": 610, "m": 377, "ñ": 233, "n": 233, "ô": 144, "ó": 144, "ò": 144,
    "õ": 144, "o": 144, "þ": 89, "p": 89, "q": 55, "r": 34, "š": 21, "s": 21,
    "t": 13, "ú": 8, "û": 8, "u": 8, "v": 5, "w": 3, "x": 2, "ü": 1, "y": 1,
    "ž": 1, "z": 1, "å": 121393, "æ": 121393, "ä": 121393, "ø": 144, "ö": 144
};

/**
 * Get cipher mapping by cipher ID
 * @param {string} cipherID - The cipher identifier
 * @returns {Object} The cipher mapping object
 */
function getCipher(cipherID) {
    return cipher[cipherID];
}