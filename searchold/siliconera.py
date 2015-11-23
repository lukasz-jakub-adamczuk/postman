#!/bin/python

import time, datetime

def parse(soup, res):
    news = soup.findAll('div')

    # marker to make news unique by timestamp
    num = 0

    items = {}
    for item in news:
        if hasattr(item, 'get') and item.get('class') == 'post':
            elem = {}

            date = item.small.string
            pos = date.index('.')+2

            container = item.h2.a.contents
            title = ''
            for itm in container:
                title += itm.string

            container = item.p.findNextSibling('p').contents
            desc = ''
            for itm in container:
                desc += itm.string

            # print title
            num += 1
            
            elem['title'] = title
            elem['desc'] = desc
            elem['link'] = item.h2.a.get('href')
            elem['date'] = date[pos:]

            # September 17, 2014 . 9:01am
            ts = time.mktime(datetime.datetime.strptime(elem['date'], "%B %d, %Y . %M:%S%p").timetuple())

            # print ts

            items[str(int(ts)+num)] = elem

            # items.append(elem)

    # return items

    collection = []
    for key in sorted(items, reverse=True):
        collection.append(items[key])

    return collection