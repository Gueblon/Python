from bs4 import BeautifulSoup
import requests


def parsecalend():
    url='https://www.calend.ru/'
    s = requests.get(url)
    calend =''
    soup = BeautifulSoup(s.text, 'lxml')
    ads = soup.find('div', class_='block holidays').find_all('div', class_='caption')
    for ad in ads:
        try:
            datе = ad.find('span', class_='title')
            datе = datе.a.text
        except:
            datе = ''
        calend = calend + datе +'.\n'
    return calend

def main ():
    print (parsecalend())

if __name__ == '__main__':
    main()
