from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/exercises/exercise1.html')
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.h1)