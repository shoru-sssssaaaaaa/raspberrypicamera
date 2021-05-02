#!/bin/sh -l
wget -O ./image.jpg http://$ID:$PW@localhost:8080/?action=snapshot
