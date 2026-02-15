#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to generate the NZBGeek Post executable using PyInstaller
"""

import os
import sys
import subprocess
from pathlib import Path

# Configure encoding to support emojis on Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


def build_executable():
    """Compiles Python script into Windows executable"""
    
    print("=" * 70)
    print("NZBGeek Post - Build Script v1.1.1")
    print("=" * 70)
    print()
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("[OK] PyInstaller found")
    except ImportError:
        print("[ERROR] PyInstaller not found!")
        print("\nInstalling PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("[OK] PyInstaller installed successfully")
    
    print()
    print("Generating executable...")
    print()
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single file
        "--console",                    # Console mode (not GUI)
        "--name=nzbgeek-post",          # Executable name
        "--icon=NONE",                  # No custom icon
        "--clean",                      # Clean cache before build
        "--noconfirm",                  # Don't ask for confirmation
        "nzbgeek-post.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print()
        print("=" * 70)
        print("[OK] Executable created successfully!")
        print("=" * 70)
        print()
        print("Location: dist/nzbgeek-post.exe")
        print()
        print("Next steps:")
        print("1. Test the executable: dist\\nzbgeek-post.exe")
        print("2. If it works, create a release on GitHub")
        print("3. Attach the .exe file to the release")
        print()
        
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error generating executable: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(build_executable())
