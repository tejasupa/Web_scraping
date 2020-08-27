import requests
from bs4 import BeautifulSoup as bs
session, url = requests.session(), "https://www.carwale.com/mg-cars/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
a = session.get(url, headers=headers)
soup = bs(a.text, 'html.parser')
print(*[car_detail.find('h2').string for car_detail in soup.findAll('li', {'class': 'o-fzptUA'})], sep='\n')
