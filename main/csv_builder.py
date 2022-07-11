import requests
import json
import csv

url = "https://stock-market-data.p.rapidapi.com/stock/historical-prices"
# CHANGE HEADER
headers = {
    "X-RapidAPI-Key": "86aa6a3740msha716886d7506c01p1032b1jsn4a7ce817ea44",
    "X-RapidAPI-Host": "stock-market-data.p.rapidapi.com"
}


def build_csv(data, name):
   # create df and then remove index
    data_file = open(f'../CSV/{name}.csv', 'w', newline='', index=False)
    csv_writer = csv.writer(data_file)
    count = 0
    for data in data:
        data['country'] = name
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(data.values())

    print(f"csv created for {name}")
    data_file.close()


with open('../Stocks.json') as f:
    ls = json.load(f)

for stock_name in ls:
    querystring = {"ticker_symbol": stock_name, "years": "1", "format": "json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    jdata = response.json()
    jdata = jdata['historical prices']
    build_csv(jdata, stock_name)
