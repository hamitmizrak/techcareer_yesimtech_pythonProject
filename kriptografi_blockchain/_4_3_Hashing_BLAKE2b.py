# pip install pycryptodome
# Eğer yükleme olmazsa;
# pip uninstall pycryptodome
# pip install pycryptodome --no-cache-dir
import hashlib

data = "Bu bir hashing örneğidir.".encode()

blake2b_hash = hashlib.blake2b(data).hexdigest()
print("BLAKE2b Hash:", blake2b_hash)
