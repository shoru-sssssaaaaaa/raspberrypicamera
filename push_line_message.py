import os
import requests
import subprocess
from subprocess import PIPE

def lineNotify(message):
    line_notify_token = os.environ.get('LINE_TOKEN1')
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)
proc = subprocess.run("downloadimage.sh", shell=True, text=True)
lineNotify('(・ω・)')
