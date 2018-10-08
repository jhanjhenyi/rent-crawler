import json
import requests


API_URL = "https://rent.591.com.tw/home/search/rsList"
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
}


session = requests.session()


def get_houses():

    response = session.get(url=API_URL, headers=HEADERS)
    data = response.json()['data']['data']
    
    houses = []
    for house in data:
        title = house.get('address_img_title')
        price = house.get('price')
        type = house.get('kind_name')

        houses.append({
            'title': title,
            'price': price,
            'type': type
        })

    return houses


def dump_json(data):
    with open("data.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    dump_json(get_houses())
