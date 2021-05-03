import os
import requests
import subprocess
from subprocess import PIPE


def lineNotify(message, *args):
    line_notify_token = os.environ.get("LINE_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    payload = {"message": message}
    headers = {"Authorization": "Bearer " + line_notify_token}
    if len(args) == 0:
        requests.post(line_notify_api, data=payload, headers=headers)
    else:
        files = {"imageFile": open(args[0], "rb")}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

directory = os.environ.get("DIR")
proc = subprocess.run(directory + "/downloadimage.sh", shell=True)
print("Image downloaded")
lineNotify("(・ω・)", directory + "/image.jpg")
print("Pushed a LINE message")
os.remove(directory + "/image.jpg")
print("Delete an image file")
