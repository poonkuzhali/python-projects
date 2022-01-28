import os

import requests
import shutil
import subprocess


def get_random_cat_image():
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    img = requests.get(url=url, stream=True)
    return img.raw


def save_image(data, folder, name):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as f:
        shutil.copyfileobj(data, f)


def open_folder(folder):
    subprocess.call(['open', folder])
