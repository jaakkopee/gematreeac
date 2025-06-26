# GemaTreeAC 2=0 JavaScript Port

This repository contains a complete port of the GemaTreeAC 2=0 Gematria Calculator from PyScript to native JavaScript.

## Overview

GemaTreeAC 2=0 is a gematria calculator, numerological classification algorithm and database that has been successfully ported from Python/PyScript to pure JavaScript, maintaining all core functionality while removing dependencies on Python runtime.

## Files Structure

### Original Files (Preserved)
- `GemaTreeAC_index_original.html` - Original PyScript version
- `GemaTreeAC_index_backup.html` - Backup of the original
- Python modules (`alphabet.py`, `gemNumFuncs.py`, etc.) - Original Python implementations

### JavaScript Implementation
- `GemaTreeAC_index.html` - **Main application** (now uses JavaScript)
- `js/alphabet.js` - Cipher definitions and functions
- `js/gemNumFuncs.js` - Core gematria calculation functions
- `js/getwordsfromdbs.js` - Database functions (client-side adapted)
- `js/ndigitsets3.js` - Nine-rooted tree data structure
- `js/main.js` - Main application logic and event handlers

### Testing and Demo Files
- `demo.html` - Interactive demo showcasing JavaScript functionality
- `comprehensive_test.html` - Complete test suite for all modules
- `test.html` - Basic module functionality test
- `minimal_test.html` - Minimal loading test

## Key Features Ported

### ✅ Completed
- **All cipher definitions** (ScaExt, Ord, FullR, Fibonacci, etc.)
- **Core gematria calculations** (`getGematria`, `getRootNumber`, `getParentList`)
- **Nine-rooted tree data structure** for word organization
- **Session memory management** with localStorage persistence
- **Cipher switching** with UI updates
- **Dropdown menu controls**
- **Distance measurement algorithms** (DistanceTeddyBear class)
- **Database search functions** (adapted for client-side)
- **Input validation and processing**
- **Event handling** for all UI interactions

### 🔄 Adapted Solutions
- **Syllable tokenization** - Simple JavaScript implementation replacing NLTK
- **Database storage** - In-memory arrays instead of SQLite
- **Module system** - Native JavaScript modules instead of Python imports
- **DOM manipulation** - Native JavaScript instead of PyScript

### 📝 Still Available (Optional Enhancements)
- File upload functionality
- Advanced plotting (currently basic visualization)
- Complex iframe interactions
- Advanced database features

## Usage

### Running the Application
1. Serve the files with any HTTP server:
   ```bash
   python -m http.server 8000
   # or
   npx http-server
   ```

2. Open `http://localhost:8000/GemaTreeAC_index.html` in your browser

### Testing the Implementation
- **Demo**: Open `demo.html` for an interactive demonstration
- **Full Tests**: Open `comprehensive_test.html` for complete test suite
- **Basic Tests**: Open `test.html` for basic functionality verification

## API Usage

The JavaScript modules expose a global `window.GemaTreeAC` object with all functions:

```javascript
// Calculate gematria value
const value = window.GemaTreeAC.getGematria('hello', 'ScaExt');

// Get numerological root
const root = window.GemaTreeAC.getRootNumber(123);

// Search database
const results = window.GemaTreeAC.searchDeepMemByNumberArray(100, 'ScaExt');

// Manage tree structure
window.GemaTreeAC.clearRAM();
window.GemaTreeAC.addWord('test', 'ScaExt');
const tree = window.GemaTreeAC.printAll('ScaExt');
```

## Cipher Support

All original ciphers are supported:
- **ScaExt** - English/Scandinavian Extended
- **Ord** - Ordinal
- **OrdRev** - Reverse Ordinal  
- **FullR** - Full Reduction
- **FullRRev** - Reverse Full Reduction
- **SingRed** - Single Reduction
- **SingRedRev** - Reverse Single Reduction
- **Fibonacci** - Fibonacci sequence
- **FibonacciRev** - Reverse Fibonacci

## Architecture

The JavaScript port maintains the same architectural patterns as the original:

1. **Modular Design** - Separate modules for different functionality
2. **Event-Driven** - UI interactions trigger calculations and updates
3. **Persistent State** - localStorage for session management
4. **Tree Organization** - Nine-rooted tree structure for numerological organization

## Performance Benefits

- **No Python Runtime** - Runs entirely in browser
- **Faster Loading** - No PyScript initialization overhead
- **Better Caching** - Standard JavaScript caching mechanisms
- **Wider Compatibility** - Works in any modern browser

## Browser Compatibility

Tested and working in:
- Chrome/Chromium 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Development

To modify or extend the JavaScript implementation:

1. Edit the appropriate module in the `js/` directory
2. Test changes using the test files
3. Update the main application if needed

The code is well-documented with JSDoc comments and follows modern JavaScript practices.

## License

Same as original - Copyleft 2022, Jake Pii Taivossuora, Do What Thou Wilt.

## Acknowledgments

- Original PyScript implementation by Jake Pii Taivossuora
- JavaScript port maintains fidelity to original algorithms and functionality
- Uses modern web technologies while preserving the unique numerological approach