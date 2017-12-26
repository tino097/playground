# encoding: utf-8
import requests


def download_file():
    '''Simple method that will download file '''
    fil = requests.get('https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls')
    if fil.status_code == 200:
        parse_document(fil.content)


def parse_document(data):
    '''Simple method for parsing documents'''
    with open('data.xslx', 'wb') as output:
        output.write(data)
    
    print output


if __name__ == "__main__":
    download_file()
