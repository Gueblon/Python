from bs4 import BeautifulSoup
import requests


def parseRA():
    url='https://www.residentadvisor.net/events/ru/saintpetersburg/'
    s = requests.get(url)
    RAevent =''
    soup = BeautifulSoup(s.text, 'lxml')
    ads = soup.find('ul', class_='list small clearfix popular').find_all('li', class_='')
    for ad in ads:
        try:
            datе = ad.find('article', class_='highlight-top').find('p').text.strip()
        except:
            datе = ''
        try:
            event = ad.find('article', class_='highlight-top').find('h1').text.strip()
        except:
            event = ''
        try:
            place = ad.find('article', class_='highlight-top').find('p', class_='copy nohide').text.strip()
        except:
            place = ''
        RAevent = RAevent + '\n' + datе +' '+ event +' в ' + place + '.'
    return RAevent

def main ():
    print (parseRA())

if __name__ == '__main__':
    main()
