'''
Sample application to encrypt and decrypt files using AES
'''
import os, struct
from Crypto.Cipher import AES
from Crypto import Random
import hashlib

ROOT_S3_DIR = '23344153-cloudstorage'
CHUNK_SIZE = 64 * 1024

def encrypt_file(key, file):

    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(file)

    with open(file, 'rb') as infile:
        with open(f'{file}.enc', 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '.encode("utf-8") * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, file):

    with open(file, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(f'{file}.dec', 'wb') as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

password = 'password'
key = hashlib.sha256(password.encode("utf-8")).digest()
if __name__ == '__main__':
    encrypt_file(key, "test.txt")
    decrypt_file(key, "test.txt.enc")
