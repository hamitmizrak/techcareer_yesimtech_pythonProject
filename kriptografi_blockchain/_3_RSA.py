# pip install pycryptodome
# Eğer yükleme olmazsa;
# pip uninstall pycryptodome
# pip install pycryptodome --no-cache-dir

# 3. RSA (Rivest-Shamir-Adleman) - Asimetrik Şifreleme
# RSA, asimetrik bir şifreleme algoritmasıdır ve iki anahtar (public ve private) ile çalışır.
# Şifreleme için pycryptodome kütüphanesini kullanabiliriz.

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# RSA Anahtar Üretme
key = RSA.generate(2048)  # 2048-bit RSA anahtarı üret
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Özel Anahtar (RSA):", private_key.decode())
print("Genel Anahtar (RSA):", public_key.decode())

# Veri
data = "Bu bir RSA şifreleme örneğidir.".encode()

# Şifreleme (Public Key Kullanarak)
rsa_public_key = RSA.import_key(public_key)
cipher = PKCS1_OAEP.new(rsa_public_key)
ciphertext = cipher.encrypt(data)
print("Şifrelenmiş veri (RSA):", ciphertext.hex())

# Şifre Çözme (Private Key Kullanarak)
rsa_private_key = RSA.import_key(private_key)
decipher = PKCS1_OAEP.new(rsa_private_key)
decrypted_data = decipher.decrypt(ciphertext)
print("Çözülen veri (RSA):", decrypted_data.decode())
