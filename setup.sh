#!/bin/sh -l
sudo apt-get update
sudo apt-get install -y subversion libjpeg-dev imagemagick
svn co https://svn.code.sf.net/p/mjpg-streamer/code/mjpg-streamer mjpg-streamer
cd mjpg-streamer
make
sudo make install
mkdir pics
echo "SUCCESSFULLY INSTALLED"
