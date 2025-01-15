#!/bin/bash

# Yetkilendirme
chmod +x shelling_countdown.sh

# 1.YOL
# Install
pip install matplotlib
./shelling_countdown.sh

# Update
#pip install --upgrade matplotlib
#./shelling_countdown.sh

# list
pip list
./shelling_countdown.sh

# show
pip show matplotlib

# Mevcut paketlerimizi requirement içine eklensin
pip freeze > requirements_revize.txt

###############################################################################################
# 2.YOL
# pip install -r requirements.txt