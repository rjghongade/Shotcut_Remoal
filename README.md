# Shortcut Virus Remover

This Python script helps remove shortcut viruses from a specified directory, such as a USB drive. The script scans the directory for `.lnk` files (shortcuts) and deletes them.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- Recursively scans a specified directory for shortcut files (`.lnk`)
- Deletes detected shortcut files
- Handles errors gracefully

## Technologies Used
- Python 
- OS library

## Prerequisites
- Python installed on your system
- Basic knowledge of command-line operations

## Setup
1. Clone the repository or download the script:
    ```sh
    git clone https://github.com/rjghongade/Shotcut_Remoal.git
    ```

2. Ensure Python is installed and accessible from your command line.

## Usage
1. Open the script file `os.py` and specify the path to the directory you want to scan:
    ```python
    usb_drive_path = 'F:\\'  # Replace with the correct drive letter
    ```

2. Run the script:
    ```sh
    python os.py
    ```

3. The script will recursively scan the specified path and delete any `.lnk` files it finds. It will print messages indicating which shortcuts were deleted or if there were any errors.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Contact
If you have any questions or suggestions, feel free to contact me at [rajughongade9022@gmail.com](mailto:rajughongade9022@gmail.com).

---

Thank you for using the Shortcut Virus Remover script!
