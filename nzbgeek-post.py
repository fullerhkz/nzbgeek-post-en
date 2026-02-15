#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NZBGeek Post - Submission Script
Submits .nzb files to NZBGeek indexer via API
Version: 1.1.1
"""

import os
import sys
import json
import requests
import time
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple

# Initialize colorama for Windows color support
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORS_ENABLED = True
except ImportError:
    # Fallback if colorama is not available
    COLORS_ENABLED = False
    class Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class Back:
        BLACK = RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class Style:
        BRIGHT = DIM = NORMAL = RESET_ALL = ""


# ==================== SETTINGS ====================

# Constants
API_URL = "https://api.nzbgeek.info/submit"
DEFAULT_CATEGORY = "4010"  # PC/0day

# Available categories (according to API documentation)
CATEGORIES = {
    "1": "Console",
    "2": "Movies",
    "3": "Audio",
    "4": "PC",
    "5": "TV",
    "6": "XXX",
    "7": "Books",
    "8": "Other"
}


# ==================== HELPER FUNCTIONS ====================

def print_colored(text: str, color=Fore.WHITE, style=Style.NORMAL, end='\n'):
    """
    Prints colored text
    
    Args:
        text: Text to be printed
        color: Text color (Fore.*)
        style: Text style (Style.*)
        end: End character
    """
    print(f"{style}{color}{text}{Style.RESET_ALL}", end=end)


def print_separator(char="=", length=70, color=Fore.CYAN):
    """Prints a colored separator line"""
    print_colored(char * length, color)


def print_progress_bar(current: int, total: int, prefix='', suffix='', length=50):
    """
    Displays a progress bar
    
    Args:
        current: Current value
        total: Total value
        prefix: Text before the bar
        suffix: Text after the bar
        length: Bar length
    """
    if total == 0:
        percent = 100
    else:
        percent = int(100 * (current / float(total)))
    
    filled_length = int(length * current // total) if total > 0 else length
    bar_char = '█'
    empty_char = '░'
    
    bar = bar_char * filled_length + empty_char * (length - filled_length)
    
    print(f'\r{Fore.CYAN}{prefix} {Fore.GREEN}|{bar}| {Fore.YELLOW}{percent}% {Fore.WHITE}{suffix}', end='')
    
    if current == total:
        print()  # New line when complete


def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Displays the script header with colors"""
    clear_screen()
    
    print_separator("═", 70, Fore.CYAN)
    print()
    print_colored("        ███╗   ██╗███████╗██████╗  ██████╗ ███████╗███████╗██╗  ██╗", Fore.CYAN, Style.BRIGHT)
    print_colored("        ████╗  ██║╚══███╔╝██╔══██╗██╔════╝ ██╔════╝██╔════╝██║ ██╔╝", Fore.CYAN, Style.BRIGHT)
    print_colored("        ██╔██╗ ██║  ███╔╝ ██████╔╝██║  ███╗█████╗  █████╗  █████╔╝ ", Fore.CYAN, Style.BRIGHT)
    print_colored("        ██║╚██╗██║ ███╔╝  ██╔══██╗██║   ██║██╔══╝  ██╔══╝  ██╔═██╗ ", Fore.CYAN, Style.BRIGHT)
    print_colored("        ██║ ╚████║███████╗██████╔╝╚██████╔╝███████╗███████╗██║  ██╗", Fore.CYAN, Style.BRIGHT)
    print_colored("        ╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝", Fore.CYAN, Style.BRIGHT)
    print()
    print_colored("                         Submission Tool v1.1.1", Fore.YELLOW, Style.BRIGHT)
    print()
    print_separator("═", 70, Fore.CYAN)


def get_api_key() -> Optional[str]:
    """
    Gets the API key from environment variable
    
    Returns:
        str: API key or None if not found
    """
    api_key = os.environ.get('NZBGEEK_API_KEY')
    
    if not api_key:
        print()
        print_colored("❌ [ERROR] API key not found!", Fore.RED, Style.BRIGHT)
        print_colored("Please set the 'NZBGEEK_API_KEY' environment variable", Fore.YELLOW)
        print()
        print_colored("To set on Windows:", Fore.CYAN)
        print_colored("  setx NZBGEEK_API_KEY \"your_api_key_here\"", Fore.WHITE)
        print()
        print_colored("Or add via Control Panel -> System -> Environment Variables", Fore.CYAN)
        print()
        print_colored("On Linux/Mac:", Fore.CYAN)
        print_colored("  export NZBGEEK_API_KEY=\"your_api_key_here\"", Fore.WHITE)
        print_colored("  # Add to ~/.bashrc or ~/.zshrc to make it permanent", Fore.WHITE)
        return None
    
    return api_key


def get_folders() -> Tuple[Optional[Path], Optional[Path], Optional[Path]]:
    """
    Gets the source, destination and logs folders from environment variables
    
    Returns:
        Tuple: (source_folder, destination_folder, logs_folder) or (None, None, None) if any doesn't exist
    """
    submission_folder = os.environ.get('NZBGEEK_SUBMISSION_FOLDER')
    complete_folder = os.environ.get('NZBGEEK_COMPLETE_FOLDER')
    log_folder = os.environ.get('NZBGEEK_LOG_FOLDER')
    
    if not submission_folder:
        print()
        print_colored("❌ [ERROR] Submission folder not configured!", Fore.RED, Style.BRIGHT)
        print_colored("Set the 'NZBGEEK_SUBMISSION_FOLDER' environment variable", Fore.YELLOW)
        return None, None, None
    
    if not complete_folder:
        print()
        print_colored("❌ [ERROR] Destination folder not configured!", Fore.RED, Style.BRIGHT)
        print_colored("Set the 'NZBGEEK_COMPLETE_FOLDER' environment variable", Fore.YELLOW)
        return None, None, None
    
    if not log_folder:
        print()
        print_colored("❌ [ERROR] Log folder not configured!", Fore.RED, Style.BRIGHT)
        print_colored("Set the 'NZBGEEK_LOG_FOLDER' environment variable", Fore.YELLOW)
        return None, None, None
    
    submission_path = Path(submission_folder)
    complete_path = Path(complete_folder)
    log_path = Path(log_folder)
    
    # Check if source folder exists
    if not submission_path.exists():
        print()
        print_colored(f"❌ [ERROR] Source folder not found: '{submission_path}'", Fore.RED, Style.BRIGHT)
        return None, None, None
    
    # Create destination folder if it doesn't exist
    if not complete_path.exists():
        print_colored(f"📁 [INFO] Creating destination folder: '{complete_path}'", Fore.BLUE)
        try:
            complete_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print_colored(f"❌ [ERROR] Could not create destination folder: {e}", Fore.RED, Style.BRIGHT)
            return None, None, None
    
    # Create logs folder if it doesn't exist
    if not log_path.exists():
        print_colored(f"📝 [INFO] Creating logs folder: '{log_path}'", Fore.BLUE)
        try:
            log_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print_colored(f"❌ [ERROR] Could not create logs folder: {e}", Fore.RED, Style.BRIGHT)
            return None, None, None
    
    return submission_path, complete_path, log_path


def select_category() -> Optional[str]:
    """
    Allows user to select a category
    
    Returns:
        str: Selected category ID, or None if user chose to exit
    """
    print()
    print_separator("─", 70, Fore.CYAN)
    print_colored("📋 Select the category for NZB files:", Fore.CYAN, Style.BRIGHT)
    print_separator("─", 70, Fore.CYAN)
    print()
    
    # List main categories with colors
    print_colored("  1", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - Console", Fore.WHITE)
    
    print_colored("  2", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - Movies", Fore.WHITE)
    
    print_colored("  3", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - Audio", Fore.WHITE)
    
    print_colored("  4", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - PC (Applications)", Fore.WHITE)
    
    print_colored("  5", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - TV (Series)", Fore.WHITE)
    
    print_colored("  6", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - XXX (Adult)", Fore.WHITE)
    
    print_colored("  7", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - Books", Fore.WHITE)
    
    print_colored("  8", Fore.YELLOW, Style.BRIGHT, end="")
    print_colored(" - Other", Fore.WHITE)
    
    print()
    print_colored("  9", Fore.GREEN, Style.BRIGHT, end="")
    print_colored(" - Use default (PC/0day - 4010)", Fore.GREEN)
    
    print()
    print_colored("  0", Fore.RED, Style.BRIGHT, end="")
    print_colored(" - Exit program", Fore.RED)
    
    print()
    print_separator("─", 70, Fore.CYAN)
    
    while True:
        print()
        print_colored("Enter category number (0-9): ", Fore.CYAN, end="")
        choice = input().strip()
        
        if choice == "0":
            return None  # Signal to exit
        
        if choice == "9":
            return DEFAULT_CATEGORY
        
        if choice in CATEGORIES:
            # Allow entering subcategory if needed
            print()
            print_colored(f"✓ You selected: {CATEGORIES[choice]}", Fore.GREEN, Style.BRIGHT)
            print_colored("Enter full subcategory ID (or ENTER to use main category only): ", Fore.CYAN, end="")
            sub = input().strip()
            
            if sub:
                return sub
            else:
                return f"{choice}000"  # Main category
        
        print_colored("❌ Invalid option! Enter a number between 0 and 9.", Fore.RED, Style.BRIGHT)


def write_log(log_file: Path, message: str):
    """
    Writes a message to the log file
    
    Args:
        log_file: Path to log file
        message: Message to be written
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} {message}\n")
    except Exception as e:
        print_colored(f"⚠️  [WARNING] Error writing to log: {e}", Fore.YELLOW)


def submit_nzb(nzb_file: Path, api_key: str, category: Optional[str] = None) -> Tuple[bool, str]:
    """
    Submits an NZB file to NZBGeek
    
    Args:
        nzb_file: Path to NZB file
        api_key: NZBGeek API key
        category: Category ID (optional)
    
    Returns:
        Tuple: (success: bool, response: str)
    """
    try:
        # Prepare URL with API key
        url = f"{API_URL}?apikey={api_key}"
        
        # Add category if provided
        if category:
            url += f"&cat={category}"
        
        # Prepare file for upload
        with open(nzb_file, 'rb') as f:
            files = {'nzb': (nzb_file.name, f, 'application/x-nzb')}
            
            # Send request
            response = requests.post(url, files=files, timeout=60, verify=False)
            response.raise_for_status()
            
            # Return result
            return True, response.text
            
    except requests.exceptions.RequestException as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


def process_nzbs(submission_folder: Path, complete_folder: Path, log_folder: Path, 
                 api_key: str, category: str) -> int:
    """
    Processes all NZB files in the submission folder
    
    Args:
        submission_folder: Folder containing NZB files
        complete_folder: Folder where files will be moved after sending
        log_folder: Folder where logs will be saved
        api_key: NZBGeek API key
        category: Category ID
    
    Returns:
        int: Number of files successfully sent
    """
    # Create daily log file
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = log_folder / f"submit_log_{today}.txt"
    
    # Display settings
    print()
    print_separator("═", 70, Fore.MAGENTA)
    print_colored("                     📋 SETTINGS", Fore.MAGENTA, Style.BRIGHT)
    print_separator("═", 70, Fore.MAGENTA)
    print()
    
    print_colored("  📂 Source folder:      ", Fore.CYAN, end="")
    print_colored(str(submission_folder), Fore.WHITE)
    
    print_colored("  📁 Destination folder: ", Fore.CYAN, end="")
    print_colored(str(complete_folder), Fore.WHITE)
    
    print_colored("  📝 Today's log:        ", Fore.CYAN, end="")
    print_colored(log_file.name, Fore.WHITE)
    
    print_colored("  🔖 Category:           ", Fore.CYAN, end="")
    print_colored(f"ID {category}", Fore.YELLOW, Style.BRIGHT)
    
    print()
    print_separator("═", 70, Fore.MAGENTA)
    print()
    
    # Confirmation
    print_colored("Press ENTER to start sending NZB files, or CTRL+C to cancel.", Fore.GREEN, Style.BRIGHT)
    input()
    
    # List NZB files
    nzb_files = list(submission_folder.glob("*.nzb"))
    
    if not nzb_files:
        print()
        print_colored("⚠️  No NZB files found to send.", Fore.YELLOW, Style.BRIGHT)
        write_log(log_file, "No NZB files found.")
        return 0
    
    # Display processing information
    total_files = len(nzb_files)
    print()
    print_separator("─", 70, Fore.CYAN)
    print_colored(f"📦 Total files found: {total_files}", Fore.CYAN, Style.BRIGHT)
    print_separator("─", 70, Fore.CYAN)
    print()
    
    # Process each file
    success_count = 0
    
    for idx, nzb_file in enumerate(nzb_files, 1):
        print()
        print_separator("─", 70, Fore.BLUE)
        print_colored(f"📤 [{idx}/{total_files}] Sending: ", Fore.CYAN, Style.BRIGHT, end="")
        print_colored(nzb_file.name, Fore.WHITE, Style.BRIGHT)
        print_separator("─", 70, Fore.BLUE)
        
        write_log(log_file, f"[{idx}/{total_files}] Sending: {nzb_file.name} (Category: {category})")
        
        # Simulate progress bar during upload
        print_colored("Uploading...", Fore.YELLOW)
        for i in range(11):
            print_progress_bar(i, 10, prefix='Progress:', suffix='', length=40)
            time.sleep(0.05)  # Small delay for visualization
        
        # Submit file
        success, response = submit_nzb(nzb_file, api_key, category)
        
        if success:
            write_log(log_file, f"Response: {response}")
            
            # Check if submission was successful
            try:
                response_json = json.loads(response)
                if response_json.get('response', {}).get('@attributes', {}).get('REGISTER') == 'OK':
                    print()
                    print_colored("✅ Successfully sent!", Fore.GREEN, Style.BRIGHT)
                    
                    # Move file to completed folder
                    try:
                        destination = complete_folder / nzb_file.name
                        
                        # Remove existing file if necessary
                        if destination.exists():
                            destination.unlink()
                        
                        nzb_file.rename(destination)
                        print_colored(f"   ➜ Moved to: ", Fore.CYAN, end="")
                        print_colored(str(destination), Fore.WHITE)
                        write_log(log_file, f"Moved to: {destination}")
                        success_count += 1
                        
                    except Exception as e:
                        print()
                        print_colored(f"❌ [ERROR] Failed to move file: {e}", Fore.RED, Style.BRIGHT)
                        write_log(log_file, f"[ERROR] Failed to move file: {e}")
                else:
                    print()
                    print_colored(f"⚠️  Unexpected API response: {response}", Fore.YELLOW)
                    write_log(log_file, f"[WARNING] Unexpected response: {response}")
                    
            except json.JSONDecodeError:
                print()
                print_colored(f"⚠️  Could not parse response: {response}", Fore.YELLOW)
                write_log(log_file, f"[WARNING] Non-JSON response: {response}")
        else:
            print()
            print_colored(f"❌ [ERROR] Submission failed: {response}", Fore.RED, Style.BRIGHT)
            write_log(log_file, f"[ERROR] Submission failed: {response}")
    
    return success_count


def main():
    """Main function"""
    try:
        while True:
            # Display header
            print_header()
            
            # Get settings
            api_key = get_api_key()
            if not api_key:
                print()
                print_colored("Press ENTER to exit...", Fore.CYAN)
                input()
                return 1
            
            submission_folder, complete_folder, log_folder = get_folders()
            if not submission_folder:
                print()
                print_colored("Press ENTER to exit...", Fore.CYAN)
                input()
                return 1
            
            # Select category
            category = select_category()
            
            # If user chose to exit
            if category is None:
                print()
                print_colored("👋 Goodbye!", Fore.CYAN, Style.BRIGHT)
                time.sleep(1)
                return 0
            
            # Process NZB files
            success_count = process_nzbs(
                submission_folder, 
                complete_folder, 
                log_folder, 
                api_key, 
                category
            )
            
            # Display result
            print()
            print_separator("═", 70, Fore.GREEN)
            print_colored(f"✅ Total files successfully sent: {success_count}", Fore.GREEN, Style.BRIGHT)
            print_separator("═", 70, Fore.GREEN)
            print_colored("            PROCESSING COMPLETED", Fore.GREEN, Style.BRIGHT)
            print_separator("═", 70, Fore.GREEN)
            
            # Ask if user wants to continue
            print()
            print()
            print_colored("What would you like to do now?", Fore.CYAN, Style.BRIGHT)
            print()
            print_colored("  1", Fore.YELLOW, Style.BRIGHT, end="")
            print_colored(" - Check again for new NZBs", Fore.WHITE)
            print_colored("  0", Fore.RED, Style.BRIGHT, end="")
            print_colored(" - Exit program", Fore.RED)
            
            while True:
                print()
                print_colored("Enter your option (0-1): ", Fore.CYAN, end="")
                choice = input().strip()
                
                if choice == "0":
                    print()
                    print_colored("👋 Goodbye!", Fore.CYAN, Style.BRIGHT)
                    time.sleep(1)
                    return 0
                elif choice == "1":
                    break
                else:
                    print_colored("❌ Invalid option! Enter 0 or 1.", Fore.RED, Style.BRIGHT)
    
    except KeyboardInterrupt:
        print()
        print()
        print_colored("⚠️  Script interrupted by user.", Fore.YELLOW, Style.BRIGHT)
        time.sleep(2)
        return 130
    except Exception as e:
        print()
        print()
        print_colored(f"❌ [CRITICAL ERROR] {e}", Fore.RED, Style.BRIGHT)
        print()
        print_colored("Press ENTER to exit...", Fore.CYAN)
        input()
        return 1


if __name__ == "__main__":
    sys.exit(main())
