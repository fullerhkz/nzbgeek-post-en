# NZBGeek Post

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Portuguese Version](https://img.shields.io/badge/🇧🇷_versão-português-green)](https://github.com/fullerhkz/nzbgeek-post)

Python script to submit `.nzb` files to the **NZBGeek** indexer via official API.

> **🇧🇷 Versão em Português:** [nzbgeek-post](https://github.com/fullerhkz/nzbgeek-post)

## 📋 Table of Contents

- [Description](#-description)
- [Features](#-features)
- [Download](#-download)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#️-configuration)
  - [Environment Variables](#environment-variables)
  - [How to Configure on Windows](#how-to-configure-on-windows)
  - [How to Configure on Linux/Mac](#how-to-configure-on-linuxmac)
- [Usage](#-usage)
- [Available Categories](#-available-categories)
- [Compiling the Executable](#-compiling-the-executable)
- [Project Structure](#-project-structure)
- [NZBGeek API](#-nzbgeek-api)
- [Logs](#-logs)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

> [!NOTE]
> ## 🎯 Description
> 
> This script automates the submission of `.nzb` files to **NZBGeek**, a popular indexer on the decentralized Usenet network. Designed to facilitate community contribution, it offers a modern, colorful interface for batch submissions, interactive category selection, detailed logs, and real-time visual feedback.
> 
> **Ideal for:** Usenet users who want to contribute to the NZBGeek indexer quickly and efficiently.

**Main Features:**
- ✅ Modern colorful interface with progress bars (v1.1.0+)
- ✅ Automatic batch submission of multiple NZB files
- ✅ Interactive category selection
- ✅ Automatic file movement after processing
- ✅ Detailed logging system with timestamps
- ✅ Real-time visual feedback with contextual colors
- ✅ Configuration via environment variables (secure)
- ✅ Robust error handling
- ✅ Standalone executable (.exe) available

## ✨ Features

- **Colorful Visual Interface**: ASCII art with vibrant colors and progress bars (v1.1.0+)
- **Security**: API key stored in environment variable (not in code)
- **Organization**: Automatically moves processed files to separate folder
- **Daily Logs**: Records all operations with timestamp
- **Categorization**: Full support for NZBGeek API categories
- **Simple Execution**: Double-click on `.py` or `.exe` file
- **Loop Mode**: Option to process multiple times without restarting
- **Cross-platform**: Color support on Windows, Linux, and macOS

## 🆕 What's New in v1.1.1

- 🚪 **Numeric exit option** at any time (option "0")
- 🔴 **Exit highlighted in red** for better visibility
- 🤖 **Automatic terminal closure** when exiting (no need to press ENTER)
- ⌨️ **CTRL+C closes automatically** after 2 seconds
- 📊 **Expanded menu**: 0-9 (0=exit, 9=default)

## 📥 Download

### Windows Executable (.exe) - Recommended

For users who don't want to install Python, download the ready-to-use executable:

**[📦 Download Latest Version (Releases)](https://github.com/fullerhkz/nzbgeek-post-en/releases/latest)**

- ✅ No Python installation required
- ✅ Single, portable file
- ✅ Ready to use
- 🎨 Modern colorful interface (v1.1.0+)

### Python Script (.py)

For developers or those who prefer to run the source code directly:

```bash
git clone https://github.com/fullerhkz/nzbgeek-post-en.git
```

## 📦 Prerequisites

### For Executable (.exe)

- ✅ **No additional prerequisites**
- Just configure environment variables

### For Python Script (.py)

1. **Python 3.7 or higher**
   - Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - ⚠️ **IMPORTANT**: During installation, check "Add Python to PATH"

2. **Git** (optional, to clone repository)
   - Download: [https://git-scm.com/downloads](https://git-scm.com/downloads)

3. **Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Common to Both

- **NZBGeek Account**
  - Sign up at: [https://nzbgeek.info](https://nzbgeek.info)
  - Get your API key from the control panel

## 🚀 Installation

### Method 1: Using the Executable (Recommended for Users)

1. Download `nzbgeek-post.exe` from the [releases page](https://github.com/fullerhkz/nzbgeek-post-en/releases/latest)
2. Place the file in a folder of your choice
3. Configure environment variables (see below)
4. Double-click the `.exe` file

### Method 2: Cloning the Repository (For Developers)

```bash
git clone https://github.com/fullerhkz/nzbgeek-post-en.git
cd nzbgeek-post-en
pip install -r requirements.txt
```

### Method 3: Manual Script Download

1. Download the repository as ZIP
2. Extract the files
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python nzbgeek-post.py` or double-click `nzbgeek-post.py`

## ⚙️ Configuration

### Environment Variables

The script uses environment variables for configuration. **4 variables** are required:

| Variable | Description | Example |
|----------|-------------|---------|
| `NZBGEEK_API_KEY` | Your NZBGeek API key | `YourAPIKeyHere123456789` |
| `NZBGEEK_SUBMISSION_FOLDER` | Folder containing .nzb files to send | `C:\NZBs\To_Send` |
| `NZBGEEK_COMPLETE_FOLDER` | Folder where files will be moved after sending | `C:\NZBs\Sent` |
| `NZBGEEK_LOG_FOLDER` | Folder where logs will be saved | `C:\NZBs\Logs` |

### How to Configure on Windows

#### Method 1: Via Command Line (CMD)

Open **Command Prompt** as Administrator and run:

```cmd
setx NZBGEEK_API_KEY "YourAPIKeyHere123456789"
setx NZBGEEK_SUBMISSION_FOLDER "C:\Path\To\Source\Folder"
setx NZBGEEK_COMPLETE_FOLDER "C:\Path\To\Destination\Folder"
setx NZBGEEK_LOG_FOLDER "C:\Path\To\Logs\Folder"
```

**Practical example:**

```cmd
setx NZBGEEK_API_KEY "abc123def456ghi789jkl012mno345pqr"
setx NZBGEEK_SUBMISSION_FOLDER "C:\Users\YourUser\NZBs\Submit"
setx NZBGEEK_COMPLETE_FOLDER "C:\Users\YourUser\NZBs\Completed"
setx NZBGEEK_LOG_FOLDER "C:\Users\YourUser\NZBs\Logs"
```

⚠️ **Important**: After configuring variables, **close and reopen the terminal** for changes to take effect.

#### Method 2: Via Windows GUI

1. Press `Win + Pause/Break` or right-click "This PC" → "Properties"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. In the "User variables" section, click "New"
5. Add each variable:
   - **Variable name**: `NZBGEEK_API_KEY`
   - **Variable value**: Your API key
6. Repeat for the other 3 variables
7. Click "OK" to save

#### Method 3: Via PowerShell

Open **PowerShell** as Administrator and run:

```powershell
[Environment]::SetEnvironmentVariable("NZBGEEK_API_KEY", "YourAPIKeyHere123456789", "User")
[Environment]::SetEnvironmentVariable("NZBGEEK_SUBMISSION_FOLDER", "C:\Path\To\Source\Folder", "User")
[Environment]::SetEnvironmentVariable("NZBGEEK_COMPLETE_FOLDER", "C:\Path\To\Destination\Folder", "User")
[Environment]::SetEnvironmentVariable("NZBGEEK_LOG_FOLDER", "C:\Path\To\Logs\Folder", "User")
```

### How to Configure on Linux/Mac

#### Method 1: Temporary (Current Session Only)

```bash
export NZBGEEK_API_KEY="YourAPIKeyHere123456789"
export NZBGEEK_SUBMISSION_FOLDER="/path/to/source/folder"
export NZBGEEK_COMPLETE_FOLDER="/path/to/destination/folder"
export NZBGEEK_LOG_FOLDER="/path/to/logs/folder"
```

#### Method 2: Permanent (All Sessions)

Add to `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

```bash
# NZBGeek Post Configuration
export NZBGEEK_API_KEY="YourAPIKeyHere123456789"
export NZBGEEK_SUBMISSION_FOLDER="/home/youruser/nzbs/submit"
export NZBGEEK_COMPLETE_FOLDER="/home/youruser/nzbs/completed"
export NZBGEEK_LOG_FOLDER="/home/youruser/nzbs/logs"
```

Then reload the configuration:

```bash
source ~/.bashrc  # or ~/.zshrc
```

### Checking Configuration

To verify if variables were configured correctly, open a **new terminal** and run:

**Windows (CMD):**
```cmd
echo %NZBGEEK_API_KEY%
```

**Windows (PowerShell):**
```powershell
$env:NZBGEEK_API_KEY
```

**Linux/Mac:**
```bash
echo $NZBGEEK_API_KEY
```

**Python:**
```python
python -c "import os; print(os.environ.get('NZBGEEK_API_KEY'))"
```

## 💻 Usage

### Using the Executable (.exe)

1. Locate the `nzbgeek-post.exe` file
2. **Double-click** the file
3. Follow the on-screen instructions

### Using the Python Script (.py)

**Double Click:**
- Simply double-click `nzbgeek-post.py`

**Via Terminal:**
```bash
python nzbgeek-post.py
```

### Usage Flow

1. **Select Category**: The script will present a menu with available categories
2. **Confirmation**: Press ENTER to start sending
3. **Processing**: Files will be sent one by one
4. **Movement**: Successfully sent files are moved to the completed folder
5. **Logs**: All operations are recorded in the daily log file
6. **Repeat or Exit**: Choose whether to process more files or exit

## 📂 Available Categories

The script supports the following main categories:

| ID | Category | Description |
|----|----------|-------------|
| 1xxx | Console | Console games |
| 2xxx | Movies | Movies |
| 3xxx | Audio | Music and audio |
| 4xxx | PC | PC applications and games |
| 5xxx | TV | TV series and shows |
| 6xxx | XXX | Adult content |
| 7xxx | Books | Books and magazines |
| 8xxx | Other | Others |

### Default Category

If you press `9` in the category menu, the default category will be used:
- **4010**: PC/0day (PC Applications)

### Subcategories

You can specify an exact subcategory by entering the full ID when prompted. Consult the [NZBGeek API capabilities page](https://nzbgeek.info/api) for the complete list of subcategories.

## 🔨 Compiling the Executable

If you want to generate your own executable from source code:

```bash
# Install dependencies (including PyInstaller)
pip install -r requirements.txt

# Run the build script
python build_exe.py
```

The executable will be created at: `dist/nzbgeek-post.exe`

### Manual Build with PyInstaller

```bash
pyinstaller --onefile --console --name=nzbgeek-post nzbgeek-post.py
```

## 📁 Project Structure

```
nzbgeek-post-en/
│
├── nzbgeek-post.py        # Main Python script
├── build_exe.py           # Script to generate executable
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guide
├── LICENSE                # Project license (MIT)
├── .gitignore             # Files ignored by git
│

```

## 🔌 NZBGeek API

### Endpoint

```
https://api.nzbgeek.info/submit
```

### Parameters

- `apikey` (required): Your API key
- `cat` (optional): Category ID
- `nzb` (required): NZB file (multipart/form-data)
- `nfo` (optional): NFO file (multipart/form-data)

### Success Response

```json
{
  "response": {
    "@attributes": {
      "API": "OK",
      "REGISTER": "OK"
    }
  }
}
```

### Response with NFO

```json
{
  "response": {
    "@attributes": {
      "API": "OK",
      "NFO": "OK",
      "REGISTER": "OK"
    }
  }
}
```

## 📝 Logs

Logs are saved daily in the folder configured in `NZBGEEK_LOG_FOLDER`.

### File Name Format

```
submit_log_YYYY-MM-DD.txt
```

Example: `submit_log_2026-02-15.txt`

### Log Content

```
2026-02-15 22:15:30 [1/3] Sending: file1.nzb (Category: 4010)
2026-02-15 22:15:32 Response: {"response":{"@attributes":{"API":"OK","REGISTER":"OK"}}}
2026-02-15 22:15:32 Moved to: C:\NZBs\Completed\file1.nzb
2026-02-15 22:15:35 [2/3] Sending: file2.nzb (Category: 4010)
2026-02-15 22:15:37 [ERROR] Submission failed: Connection timeout
```

## 🔧 Troubleshooting

### Error: "Python not found" (for .py only)

**Cause**: Python is not installed or not in system PATH.

**Solution**:
1. Download and install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Restart terminal

**Alternative**: Use the `.exe` executable which doesn't require Python installation.

### Error: "API key not found"

**Cause**: The `NZBGEEK_API_KEY` environment variable is not configured.

**Solution**:
1. Configure the variable as per [Configuration](#️-configuration) section
2. Close and reopen terminal/application
3. Verify configuration with: `echo %NZBGEEK_API_KEY%` (Windows) or `echo $NZBGEEK_API_KEY` (Linux/Mac)

### Error: "Submission folder not found"

**Cause**: The path configured in `NZBGEEK_SUBMISSION_FOLDER` doesn't exist.

**Solution**:
1. Check if the path is correct
2. Create the folder manually
3. Reconfigure the environment variable with the correct path

### Error: "ModuleNotFoundError: No module named 'requests'" (for .py only)

**Cause**: The `requests` library is not installed.

**Solution**:
```bash
pip install requests
```

or

```bash
pip install -r requirements.txt
```

**Alternative**: Use the `.exe` executable which already includes all dependencies.

### SSL/Certificate Warnings

**Cause**: The script disables SSL verification to avoid certificate issues.

**Solution**: This is intentional and safe for the NZBGeek API. If you want to enable SSL verification, edit this line in the script:
```python
response = requests.post(url, files=files, timeout=60, verify=True)
```

### Files are not moved after sending

**Cause**: Insufficient permissions or destination folder in use.

**Solution**:
1. Check folder permissions
2. Make sure no other program is using the files
3. Run the script as Administrator if necessary

### Executable blocked by Windows Defender

**Cause**: Compiled Python executables are sometimes flagged as suspicious.

**Solution**:
1. Add exception in Windows Defender
2. Or compile it yourself using `build_exe.py`
3. Or use the `.py` script directly

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute.

### How to Create a Release

For project maintainers:

1. Compile the executable: `python build_exe.py`
2. Test the executable: `dist\nzbgeek-post.exe`
3. Create a tag: `git tag v1.1.1`
4. Push the tag: `git push origin v1.1.1`
5. Create a release on GitHub
6. Attach the `nzbgeek-post.exe` file to the release

## 📄 License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

---

## 📞 Support

If you encounter issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Consult the [NZBGeek API documentation](https://nzbgeek.info/api)
3. Open an [issue on GitHub](https://github.com/fullerhkz/nzbgeek-post-en/issues)

---

## 🌟 Acknowledgments

- Original PowerShell script developed for personal use
- API provided by [NZBGeek](https://nzbgeek.info)
- `requests` library by the Requests project developers
- PyInstaller for executable generation
- Thanks to the Usenet community

---

## 🌐 Other Languages

- **🇧🇷 Portuguese (Brasil)**: [nzbgeek-post](https://github.com/fullerhkz/nzbgeek-post)
- **🇺🇸 English**: You are here!

---

<div align="center">

**Developed with ❤️ for the Usenet community**

[⬆ Back to top](#nzbgeek-post)

</div>
