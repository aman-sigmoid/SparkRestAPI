import json

import requests

def get_stocks():
    url = "https://stock-market-data.p.rapidapi.com/market/index/s-and-p-six-hundred"

    headers = {
        "X-RapidAPI-Key": "86aa6a3740msha716886d7506c01p1032b1jsn4a7ce817ea44",
        "X-RapidAPI-Host": "stock-market-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()


data = get_stocks()

with open('../Stocks.json', 'w') as convert_file:
    convert_file.write(json.dumps(data['stocks'][:25]))
