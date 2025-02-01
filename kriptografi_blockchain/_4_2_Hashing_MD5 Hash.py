# pip install pycryptodome
# Eğer yükleme olmazsa;
# pip uninstall pycryptodome
# pip install pycryptodome --no-cache-dir

import hashlib

data = "Bu bir hashing örneğidir.".encode()

md5_hash = hashlib.md5(data).hexdigest()
print("MD5 Hash:", md5_hash)
