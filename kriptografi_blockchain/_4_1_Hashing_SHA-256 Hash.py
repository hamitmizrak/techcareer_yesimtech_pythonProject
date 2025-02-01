# pip install pycryptodome
# Eğer yükleme olmazsa;
# pip uninstall pycryptodome
# pip install pycryptodome --no-cache-dir


# 4. Hashing (SHA-256, MD5, BLAKE2b)
# Hashing işlemi, veriyi geri döndürülemez bir özet haline getiren tek yönlü bir fonksiyondur.
# hashlib modülü ile hashing işlemlerini gerçekleştirebiliriz.


import hashlib

data = "Bu bir hashing örneğidir.".encode()

# SHA-256 Hash hesaplama
sha256_hash = hashlib.sha256(data).hexdigest()
print("SHA-256 Hash:", sha256_hash)
