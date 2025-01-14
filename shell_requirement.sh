#!/bin/bash

chmod +x shell_countdown.sh


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
