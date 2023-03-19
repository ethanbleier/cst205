from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import lxml

import ssl


ssl._create_default_https_context = ssl._create_unverified_context
my_site='https://www.rockpapershotgun.com/minecraft-house-ideas' #40 best mc house ideas

req = Request(
    my_site,
    headers={'User-Agent': 'Mozilla/5.0'}
)

resp = urlopen(req)
soup = BeautifulSoup(resp.read(), 'lxml')

print(soup.title)
# print(soup.prettify())



site_html=urlopen(my_site)

# print out a portion of the HTML
print(site_html.read()[5000:5400])

images = soup.findAll('img')
for image in images:
    print(image['src'])
