#!/bin/sh
PORT="8080"
SIZE="1280x720"
FRAMERATE="30"
export LD_LIBRARY_PATH=/usr/local/lib
export PWD=$(pwd)
echo $PWD
sudo chmod 755 $PWD/mjpg-streamer/mjpg_streamer
$PWD/mjpg-streamer/mjpg_streamer \
	-i "input_uvc.so -f $FRAMERATE -r $SIZE -d /dev/video0 -y -n" \
	-o "output_http.so -w /usr/local/www -p $PORT -c $ID:$PW" 
