import requests
from utils.config import COOKIES, URL

def get_data(day):
    url = URL.format(day)
    data = requests.get(url, headers={'Cookie': COOKIES})
    return data.text

def read_from_file():
    data = ""
    with open("input.txt", "r") as file:
        data = file.read()
    return data