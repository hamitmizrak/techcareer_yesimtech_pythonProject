#!/bin/bash

chmod +x shell_countdown.sh


################################################################

#  Hangi Yükleme Türünü Kullanmalısınız?
# Global yükleme:
#  Sistem genelinde kullanılan araçlar ve kütüphaneler için (örneğin, black, pylint gibi araçlar).
#  Yerel yükleme (local):
# Bir proje için bağımlılıkları izole etmek için. Bu en iyi uygulamadır.


# Genel Kütüphane
# Global kütüphaneler tüm projelerde kullanılabilir. Global yüklemek için bir sanal ortam (venv) aktif olmamalıdır.
# powershell : deactivate
# pip install pandas
# pip show pandas
# pip list


# local kütüphane
# Yerel yüklemeler genellikle sanal bir ortam (virtual environment) içinde yapılır.
# Bu, yalnızca o proje için geçerli olan bir kütüphane ortamı sağlar.
# powershell aç
# python -m venv venv # Sanal Ortam Oluşturma:
# venv\Scripts\activate    # Windows:
# source venv/bin/activate # MacOS/Linux:
# pip install pandas
# pip show pandas
# pip list
# pip list --local


################################################################
# Bağımlılıkları Yükleme
#pip install Flask
#pip install matplotlib
#pip install seaborn
#pip install matplotlib seaborn
pip install -r requirements.txt

pip show matplotlib
pip show seaborn


pip list
pip list --local

# Global kütüphaneler, Python sistem seviyesinde (tüm projeler için) yüklenmiş olan kütüphanelerdir.
pip list --not-required

# Güncelleme
pip install --upgrade seaborn

# Güncellenebilir Paketleri Görüntüleme:
pip list --outdated


# Eğer mevcut yüklü paketlerinizi bir requirements.txt dosyasına kaydetmek isterseniz
# pip freeze > requirements.txt



################################################################
# Yerel (Local) Kütüphane Yüklemek
# python -m venv venv
# venv\Scripts\activate # powershell içinde yüklenir.
