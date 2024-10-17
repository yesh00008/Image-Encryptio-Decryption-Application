Image Encryption and Decryption Application
 Description
This application allows users to securely encrypt and decrypt images using various algorithms, primarily focusing on AES (Advanced Encryption Standard). The web-based interface enables easy interaction for uploading images, entering encryption keys, and downloading encrypted or decrypted images.

 Technologies Used
- **Python**: Backend logic is implemented using Python with Flask.
- **Flask**: A lightweight web framework for building web applications.
- **HTML/CSS**: Used for structuring and styling the web interface.
- **JavaScript**: Adds interactivity and handles client-side operations.
- **Pillow**: Python Imaging Library to handle image processing.
- **Cryptography**: Library for implementing secure encryption and decryption.

 Features
- Upload an image and encrypt it using AES.
- Enter a user-defined key for encryption.
- Decrypt an encrypted image using the same key.
- Download both encrypted and decrypted images.

 How to Run the Project
1. **Clone the repository**:
   
   git clone <repository-url>
   cd ImageEncryptionProject

Install the required Python packages:
pip install Flask Pillow cryptography
Run the Flask application:
python app.py
Usage Instructions
To Encrypt an Image:

Select an image file to encrypt.
Enter an encryption key.
Click "Encrypt Image" to receive the encrypted file for download.
To Decrypt an Image:

Navigate to the decryption page.
Select the encrypted file.
Enter the same encryption key used for encryption.
Click "Decrypt Image" to download the original image.
