# pip install pycryptodome
# Eğer yükleme olmazsa;
# pip uninstall pycryptodome
# pip install pycryptodome --no-cache-dir

# 2. DES (Data Encryption Standard) - Simetrik Şifreleme
# DES, AES kadar güvenli değildir ve sadece 56-bit anahtar uzunluğuna sahiptir. PyCryptodome kütüphanesi ile kullanabiliriz.

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES için 8 baytlık (64-bit) anahtar gereklidir
key = b"8bytkey1"  # 8 bayt uzunluğunda bir anahtar
iv = os.urandom(8)  # 8 bayt IV oluştur

data = "Bu bir DES şifreleme örneğidir.".encode()

# DES Şifreleme (CBC Modu)
cipher = DES.new(key, DES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(data, DES.block_size))
print("Şifrelenmiş veri (DES):", ciphertext.hex())

# DES Şifre Çözme
decipher = DES.new(key, DES.MODE_CBC, iv)
decrypted_data = unpad(decipher.decrypt(ciphertext), DES.block_size)
print("Çözülen veri (DES):", decrypted_data.decode())
