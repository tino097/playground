# encoding: utf-8
''' @author Konstantin Sivakov'''

import requests
import csv
from datetime import datetime


api_key = 'fe52241347d4855f7bc8cd70cd00cb6d'


def api_call(api_key, freq='D'):
    ''' Make API call '''
    url = 'http://api.eia.gov/series/?api_key={0}&series_id=NG.RNGWHHD.D'.format(api_key)
    result = requests.get(url)
    return result.json()


def parse_results(results):
    print type(result)
    data = result['series'][0]
    return data.get('data')


def csv_writer(data, name=None, bom=False):
    with open('results.csv', 'wb+') as csv_file:
        fieldnames = ['date', 'price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for t in data:
            date, price = datetime.strptime(t[0], '%Y%m%d'), t[1]
            row = {'date': date.date(), 'price': price}      
            writer.writerow(row)


if __name__ == '__main__':
    result = api_call(api_key, "M")
    data = parse_results(result)
    csv_writer(data)
