#!/bin/python

import time, datetime

def parse(soup, res):
    news = soup.find('div', class_='blog-grid')

    items = {}
    for item in news.contents:
        if item.name == 'article':
            if item.div.get('class'):
                if 'text' in item.div.get('class'):
                    elem = {}

                    elem['title'] = item.div.h2.a.string
                    elem['desc'] = item.div.p.string
                    elem['link'] = item.div.h2.a.get('href')
                    elem['date'] = item.div.ul.li.time.string

                    ts = time.mktime(datetime.datetime.strptime(elem['date'], "%B %d, %Y").timetuple())

                    items[str(int(ts))] = elem

    khnews = soup.find('div', class_='blog-carousel')

    for item in khnews.div:
        if item.name == 'article':
            elem = {}

            elem['title'] = item.div.h2.a.string
            elem['desc'] = '...'
            elem['link'] = item.div.h2.a.get('href')
            elem['date'] = item.div.time.string

            ts = time.mktime(datetime.datetime.strptime(elem['date'], "%B %d, %Y").timetuple())
            
            items[str(int(ts))] = elem

    collection = []
    for key in sorted(items, reverse=True):
        collection.append(items[key])

    return collection
