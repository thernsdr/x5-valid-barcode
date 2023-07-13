from dotenv import load_dotenv
import json
from os import getenv
from pdf417 import encode, render_image
import requests

load_dotenv()

card_number = getenv("CARD_NUMBER")
bearer_token = getenv("BEARER")

url = f"https://gw-el5.x5.ru/api/cards/el5.cards.CardsService/GetBarCode/{card_number}"

headers = {
    "host": "gw-el5.x5.ru",
    "connection": "keep-alive",
    "authorization": f"Bearer {bearer_token}",
    "user-agent": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
                  "Chrome/114.0.5735.196 Mobile five-browser/2.20.1.84394059 Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://homepage.5ka.ru",
    "x-requested-with": "ru.pyaterochka.app.browser",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://homepage.5ka.ru/",
    "accept-encoding": "gzip, deflate",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=headers)

raw_barcode = json.loads(response.text)["data"]["barcode"]

barcode_encoded = encode(raw_barcode, columns=3, security_level=2)
barcode_image = render_image(barcode_encoded)
barcode_image.save('barcode.jpg')
