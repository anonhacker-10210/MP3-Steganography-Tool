from Crypto.Cipher import AES
import binascii
import struct

def decrypt_message(key, encrypted_msg):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(encrypted_msg).decode('utf-8', errors='ignore')

def extract_message(mp3_file, key):
    with open(mp3_file, "rb") as file:
        mp3_data = bytearray(file.read())

    start_index = 100  # Where we stored the message length

    # Read the stored message length
    length_bytes = bytes(mp3_data[start_index:start_index + 4])
    msg_length = struct.unpack(">I", length_bytes)[0]

    chunk_size = 128
    indexes = range(200, len(mp3_data) - chunk_size, chunk_size)

    encrypted_msg = b""
    for index in indexes:
        encrypted_msg += bytes(mp3_data[index:index + chunk_size])
        if len(encrypted_msg) >= msg_length:
            encrypted_msg = encrypted_msg[:msg_length]  # Trim extra data
            break

    try:
        decrypted_msg = decrypt_message(key, encrypted_msg)
        print("Hidden Message:", decrypted_msg)
    except Exception as e:
        print("Decryption failed:", str(e))

# Default MP3 file
mp3_file = "hidden_music.mp3"

key_input = input("Enter the AES Key: ")
try:
    key = bytes.fromhex(key_input)  # Convert hex key back to bytes
    extract_message(mp3_file, key)
except binascii.Error:
    print("Invalid key format! Ensure you enter the correct AES Key.")
