# encoding: utf-8
''' @author Konstantin Sivakov'''

import requests
import json
import csv


api_key = 'fe52241347d4855f7bc8cd70cd00cb6d'


def api_call(api_key, freq='D'):
    ''' Make API call '''
    url = 'http://api.eia.gov/series/?api_key={0}&series_id=NG.RNGWHHD.D'.format(api_key)
    result = requests.get(url)
    return json.loads(result.content)

def csv_writer(res, name=None, bom=False):
    with open('results.csv', 'wb+') as csv_file:
        headers = "date, price".split(",")
        writer = csv.DictWriter(csv_file, headers, delimiter=',')
        writer.writeheader()
        series = dict(res['series'])
        data = series['data']
        print data
        # writer.writerows(res['data'])
        
if __name__ == '__main__':
    result = api_call(api_key,"M")
    csv_writer(result)
