# pip install pycryptodome
# Eğer yükleme olmazsa;
# pip uninstall pycryptodome
# pip install pycryptodome --no-cache-dir


# 1. AES (Advanced Encryption Standard) - Simetrik Şifreleme
# AES için Python'da pycryptodome kütüphanesini kullanabiliriz.
# AES, 128-bit blok boyutunda çalışır ve CBC (Cipher Block Chaining) gibi modlarla güvenliği artırabiliriz.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# 16, 24 veya 32 bayt uzunluğunda bir anahtar oluştur
key = os.urandom(32)  # 256-bit AES anahtarı
iv = os.urandom(16)   # AES için Initialization Vector (IV)

# Şifrelenecek veri
data = "Bu bir AES şifreleme örneğidir.".encode()

# AES şifreleme (CBC Modu)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(data, AES.block_size))
print("Şifrelenmiş veri (AES):", ciphertext.hex())

# AES şifre çözme
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Çözülen veri (AES):", decrypted_data.decode())
