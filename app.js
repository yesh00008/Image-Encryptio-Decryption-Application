document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData();
    const file = document.getElementById('file').files[0];
    const key = document.getElementById('encryptionKey').value; // Get the encryption key

    formData.append('file', file);
    formData.append('key', key); // Append the encryption key

    fetch('/encrypt', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const link = document.getElementById('downloadLink');
        link.href = url;
        link.style.display = 'inline-block';  // Show the download link
        document.getElementById('result').style.display = 'block';
    })
    .catch(err => console.error(err));
});

// Decrypt Image Functionality
document.getElementById('decryptForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData();
    const file = document.getElementById('decryptFile').files[0];
    const key = document.getElementById('decryptKey').value;

    formData.append('file', file);
    formData.append('key', key);

    fetch('/decrypt', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const link = document.getElementById('decryptedLink');
        link.href = url;
        link.style.display = 'inline-block';  // Show the download link for decrypted image
        document.getElementById('decryptionResult').style.display = 'block';
    })
    .catch(err => console.error(err));
});
