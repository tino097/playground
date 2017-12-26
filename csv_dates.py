# encoding: utf-8
''' simple  script to consume API data and convert to CSV file
    usage: python csv_dates.py [--api-key --freq]
'''

import requests
import csv
import argparse
from datetime import datetime

parse = argparse.ArgumentParser()
parse.add_argument('--api-key', help='Enter your api key!')
parse.add_argument('--freq', help='Frequency of prices (daily or monthly)')

args = parse.parse_args()
freq = args.freq or 'D'
api_key = args.api_key or 'fe52241347d4855f7bc8cd70cd00cb6d'

result_file = 'data/results'

if freq == 'D':
    result_file = result_file + '_daily.csv'
else:
    result_file = result_file + '_monthly.csv'


def api_call(api_key, freq='D'):
    ''' Make API call '''
    url = 'http://api.eia.gov/series/?api_key={0}&series_id=NG.RNGWHHD.{1}'.format(api_key, freq)
    result = requests.get(url)
    result.raise_for_status()
    return result.json()


def parse_results(results):
    data = results['series'][0]
    return data.get('data')


def csv_writer(data,  filename='results_daily.csv'):
    ''' csv writer method '''
    with open(filename, 'wb+') as csv_file:
        fieldnames = ['date', 'price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for t in data:
            date, price = t[0], t[1]
            if freq =='D':
                date = datetime.strptime(date, '%Y%m%d')
            else:
                date = datetime.strptime(t[0], '%Y%m')
            row = {'date': date.date(), 'price': price}      
            writer.writerow(row)


if __name__ == '__main__':
    result = api_call(api_key, freq)
    data = parse_results(result)
    csv_writer(data, filename=result_file)
