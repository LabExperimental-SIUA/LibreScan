#!/usr/bin/env bash
apt-get -y install python3-pip lua5.2 liblua5.2 libusb-dev python3 python-dev libjpeg libjpeg-dev libssl-dev libffi-dev libturbojpeg1-dev libyaml-dev
pip3 install pyYAML bottle pyjade jinja2 polib cffi pexpect
pip3 install jpegtran-cffi==0.5.2

apt-get -y install tesseract-ocr tesseract-ocr-spa

apt-get -y install scantailor

apt-get -y install ruby ruby-dev ruby-rmagick 
gem install iconv pdfbeads

chmod +x ./chdkptp_dependency.sh
sh ./chdkptp_dependency.sh
