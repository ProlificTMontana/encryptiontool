# Description

A Python program that uses the cryptography library to encrypt and decrypt text files using a secret key. The program also includes options to save the output as a new file.

# How to Use the Program

    1.Generate a Key:
        run the program and choose option 1.
        enter a filename to save the key (e.g., mykey.key).
        the key will be saved to the specified file.

    2.Encrypt a File:
        run the program and choose option 2.
        enter the filename of the file you want to encrypt (e.g., plaintext.txt).
        enter the output filename for the encrypted file (e.g., encrypted.txt).
        enter the key file (e.g., mykey.key).
        the file will be encrypted and saved as encrypted.txt.

    3.Decrypt a File:
        run the program and choose option 3.
        enter the filename of the file you want to decrypt (e.g., encrypted.txt).
        enter the output filename for the decrypted file (e.g., decrypted.txt).
        enter the key file (e.g., mykey.key).
        the file will be decrypted and saved as decrypted.txt.

# Notes

The key is essential for both encryption and decryption. Keep it secure.
The program assumes that the input file is a text file, but it can handle any binary file.
The cryptography library uses AES encryption under the hood, which is secure for most use cases.

This program provides a simple and secure way to encrypt and decrypt files using a secret key.

Execute the script by running the .py file using python. 
