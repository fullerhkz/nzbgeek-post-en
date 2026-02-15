# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-02-15

### ✨ Added
- Numeric option "0" to exit the program in the category menu
- Automatic terminal closure when selecting exit (no need to press additional ENTER)

### 🔄 Modified
- Category menu now goes from 0-9 (option 9 for default category)
- Option "0 - Exit" highlighted in red for better visibility
- More friendly exit message ("👋 Goodbye!")
- CTRL+C interruption now closes automatically after 2 seconds

### 🐛 Fixed
- User can exit the program at any time without needing to process files

---

## [1.1.0] - 2026-02-15

### ✨ Added
- Colorful interface using `colorama` library
- Animated progress bars during file submission
- Colored visual separators for better organization
- Enhanced visual feedback with contextual colors:
  - 🟢 Green for successes
  - 🔴 Red for errors
  - 🟡 Yellow for warnings
  - 🔵 Blue for information
- Real-time file counter during processing
- Version displayed in header (v1.1.0)

### 🔄 Modified
- Renamed `submit_nzbs.py` → `nzbgeek-post.py` (standardization)
- Renamed executable from `submit_nzbs.exe` to `nzbgeek-post.exe`
- Improved visual feedback at all process stages
- Updated documentation with new names and features
- Better cross-platform compatibility with colorama

### 📦 Dependencies
- Added dependency `colorama>=0.4.6` for cross-platform color support

### 🐛 Fixes
- Better color compatibility on Windows
- Graceful fallback when colorama is not available

### 💔 Breaking Changes
- Main file renamed from `submit_nzbs.py` to `nzbgeek-post.py`
- Executable renamed from `submit_nzbs.exe` to `nzbgeek-post.exe`

---

## [1.0.0] - 2026-02-14

### 🎉 Initial Release
- Python script for submitting NZB files to NZBGeek indexer
- Console mode interface with ASCII art
- Interactive category selection
- Daily logging system
- Automatic file movement after processing
- Configuration via environment variables
- Loop mode for continuous processing
- Windows executable (.exe) generation
- Complete documentation in English
