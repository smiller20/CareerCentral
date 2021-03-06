"""
simply hired using multi process design
scrape through 11 pages of simply using a multi processing for each I/O (4x faster)
"""

from requests import get
from bs4 import BeautifulSoup
from threading import Thread
import multiprocessing
from os import getpid
import psutil

def get_simply(url, role ):
    alldata={}
    response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        content_container= soup.find_all('div', {'class': ['SerpJob-jobCard']})
        link= 'https://www.simplyhired.com'
    except AttributeError:
        pass
    for content in content_container:
        title, href=None , None
        try:
            title=content.a.text
            href=content.a['href']
            company=content.span.text
            summary=content.p.text
        except TypeError:
            pass
        except AttributeError:
            pass
        
        if title is not None and role.upper() in title.upper():
            if href is not None:
                href=link+href
                alldata[href]=[title, company, summary, href]
    return alldata 
    
def getrole_simply(role, location):
    test_data ={} 
    if "," in location:
        location=location.split(',')
        location= location[0].strip()+ "," + location[1].strip()
    url_first= 'https://www.simplyhired.com/search?q='+role+'&l='+location
    url= 'https://www.simplyhired.com/search?q='+role+'&l='+location + '&pn='
    processor_count= multiprocessing.cpu_count() #get cpu count
    pool=multiprocessing.Pool(11)
    iterable = zip( [ url +str(i)  if i != 0 else  url_first  for i in range(1,30)   ],  [role for i in range(1,30)  ] )
    result_pool=pool.starmap( get_simply, iterable) 
    pool.close() 
    pool.join()
    for i, p in enumerate(result_pool):
        for key, value in p.items():
            if value not in test_data.values():
                test_data[key]= value 
    return test_data

'''
process = psutil.Process(getpid())
print('total memory usage: ' , process.memory_info().rss , psutil.cpu_percent())  # in bytes 

'''
if __name__ == "__main__":
    getrole_simply('python', 'new jersey')