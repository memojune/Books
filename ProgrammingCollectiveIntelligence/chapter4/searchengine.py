from urllib import request, parse
from bs4 import *
class crawler:
    def __init__(self, dbname):
        pass
    
    def __del__(self):
        pass
    def __abcommit(self):
        pass

    def getentryid(self, url, soup):
        print('Indexing %s' %url)

    def addtoindex(self, soup):
        return None

    def seperatewords(self, text):
        return None

    def isindexed(self, url):
        return False

    def addlinkref(self, urlFrom, urlTo, linkText):
        pass
    
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = request.urlopen(page)
                except:
                    print('Could not open %s' %page)
                    continue
                soup = BeautifulSoup(c.read())
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):

    def createindextables(self):
        pass