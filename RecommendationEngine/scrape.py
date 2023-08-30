import requests
from bs4 import BeautifulSoup

def getLinks(keys):
    k = keys
    reviewcontainers = {}
    params = {
        'ref_': 'undefined',
        'paginationKey': ''
    }
    
    for id in k:
        url = 'https://www.imdb.com/title/' + id + '/reviews/'
        link = 'https://www.imdb.com/title/' + id + '/reviews/_ajax'
        hdr = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers = hdr)
        loadCount = 0
        
        while True:    
            f1 = open('data/'+id+'-'+str(loadCount), 'wb')
            f1.write(r.content)
            f1.close()
            loadCount += 1
            soup = BeautifulSoup(r.text, 'lxml')

            try:
                pagination_key = soup.select_one(".load-more-data[data-key]").get("data-key")
            except AttributeError:
                break
            params['paginationKey'] = pagination_key
            r = requests.get(link,params=params)

movies = ['tt0110912', 'tt1872181']

getLinks(movies)
