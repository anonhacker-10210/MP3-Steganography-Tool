# MP3 Steganography Tool

## Overview
This tool allows you to **encrypt and hide secret messages** inside MP3 files using **AES encryption** and **steganography**. It also provides a way to **extract and decrypt** the hidden messages.

## Features
- **AES Encryption (ECB Mode)** for secure message protection.
- **Steganography (Byte Manipulation)** to hide messages inside MP3 files.
- **Automatic File Input**: Reads the message from `message.txt`.
- **Extract & Decrypt Functionality**.
- **Simple CLI Interface**.

## Installation
Make sure you have Python installed and install the required libraries:
```bash
pip install pycryptodome
```

## Usage
### 1️⃣ Hide a Message in an MP3 File
- Place your **MP3 file** as `music.mp3`.
- Write your secret message inside `message.txt`.
- Run the script:
  ```bash
  python mp3_enc.py
  ```
- The encrypted message will be stored inside `hidden_music.mp3`.
- The script will output an **AES key**—**SAVE IT** (you need it for decryption).

### 2️⃣ Extract and Reveal the Hidden Message
- Run:
  ```bash
  python mp3_dec.py
  ```
- Enter the **AES Key** when prompted.
- The script will decrypt and reveal the **original hidden message**.

## File Structure
```
/MP3StegoTool
│── enc.py      # Script to hide messages in an MP3 file
│── dec.py      # Script to extract hidden messages
│── music.mp3       # Original MP3 file
│── hidden_music.mp3# MP3 file with the hidden message
│── message.txt     # Text file containing the secret message
│── README.md       # Documentation
```

## Notes
- Use a **large MP3 file** for longer messages.
- If decryption fails, **ensure you enter the correct AES key**.
- The script distributes the hidden message across multiple MP3 sections.

## License
This project is open-source and free to use!

