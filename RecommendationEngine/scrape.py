import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def getLinks(keys):
    k = [keys]
    reviewcontainers = {}
    params = {
        'ref_': 'undefined',
        'paginationKey': ''
    }
    print("Started " + keys)

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
    print("Finished " + keys)
    return k

movies = ['tt0110912', 'tt1872181', 'tt1990314', 'tt1999995']

if __name__ == '__main__':
    threads = Pool(2)
    threads.map(getLinks, movies)
