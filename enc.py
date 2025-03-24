from Crypto.Cipher import AES
import os
import struct

# Generate AES Key
key = os.urandom(16)  # 16-byte AES key

def pad_message(message):
    while len(message) % 16 != 0:
        message += " "  # Padding for AES block size
    return message

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(message.encode())

def hide_message(mp3_file, output_file, key, message):
    message = pad_message(message)  # Ensure message is 16-byte aligned
    encrypted_msg = encrypt_message(message, key)  # ✅ Fix: Now passing key

    msg_length = len(encrypted_msg)

    with open(mp3_file, "rb") as file:
        mp3_data = bytearray(file.read())

    if len(mp3_data) < msg_length + 200:
        print("MP3 file too small to hide the message.")
        return

    chunk_size = 128  # Distribute data across MP3
    indexes = range(200, len(mp3_data) - chunk_size, chunk_size)

    # Store message length first
    length_bytes = struct.pack(">I", msg_length)
    for i in range(4):
        mp3_data[100 + i] = length_bytes[i]

    # Store encrypted message across MP3 file
    for i, index in enumerate(indexes):
        if i * chunk_size >= msg_length:
            break
        mp3_data[index:index + chunk_size] = encrypted_msg[i * chunk_size:(i + 1) * chunk_size]

    with open(output_file, "wb") as file:
        file.write(mp3_data)

    print("Message hidden successfully in", output_file)
    print("Save this AES Key:", key.hex())

# Default filenames
mp3_file = "music.mp3"
output_file = "hidden_music.mp3"

# Read message from file
with open("message.txt", "r", encoding="utf-8") as file:
    message = file.read().strip()

hide_message(mp3_file, output_file, key, message)
