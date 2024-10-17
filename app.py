from flask import Flask, request, send_file
from PIL import Image
from io import BytesIO
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)

# AES Encryption Function with padding
def encrypt_image_aes(image_data, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding the image data to be a multiple of 16 bytes (AES block size)
    padding_length = 16 - (len(image_data) % 16)
    image_data += bytes([padding_length]) * padding_length
    
    encrypted_data = encryptor.update(image_data) + encryptor.finalize()
    return encrypted_data

# AES Decryption Function with unpadding
def decrypt_image_aes(encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]
    
    return decrypted_data

@app.route('/encrypt', methods=['POST'])
def encrypt_image():
    # Get the image file and key from the request
    file = request.files['file']
    key = request.form['key'].encode()  # Convert key to bytes

    # Open the image and convert to bytes
    img = Image.open(file)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_bytes = img_byte_arr.getvalue()

    # Encrypt the image
    encrypted_data = encrypt_image_aes(img_bytes, key)

    # Save the encrypted data as a binary file instead of an image
    img_io = BytesIO(encrypted_data)
    img_io.seek(0)

    return send_file(img_io, mimetype='application/octet-stream', as_attachment=True, download_name='encrypted_image.bin')

@app.route('/decrypt', methods=['POST'])
def decrypt_image():
    # Get the encrypted file and key from the request
    file = request.files['file']
    key = request.form['key'].encode()  # Get key as bytes

    # Read the encrypted file
    encrypted_data = file.read()

    # Decrypt the image data
    decrypted_data = decrypt_image_aes(encrypted_data, key)

    # Convert decrypted data back to an image
    img = Image.open(BytesIO(decrypted_data))

    # Save the decrypted image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='decrypted_image.png')

if __name__ == '__main__':
    app.run(debug=True)
