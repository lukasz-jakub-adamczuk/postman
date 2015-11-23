#!/bin/python

import time, datetime

def parse(soup, res):
    news = soup.findAll('article')

    # marker to make news unique by timestamp
    num = 0

    items = {}
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            for c in classes:
                if c == 'post':
                    elem = {}
                    # print item.div.div.h3.a.string

                    desc = ''
                    for val in list(item.div.findNextSibling('div').div.findNextSibling('div').contents):
                        desc += val.string

                    date = item.div.findNextSibling('div').header.span.string
                    pos = date.index(' on ')+4

                    num += 1
                    
                    elem['title'] = item.div.findNextSibling('div').header.h1.a.string
                    elem['desc'] = desc
                    elem['link'] = item.div.findNextSibling('div').header.h1.a.get('href')
                    elem['date'] = date[pos:]

                    parts = elem['date'].split(' ')
                    if len(parts[1]) == 1:
                        parts[1] = '0' + parts[1]

                    elem['date'] = ' '.join(parts)
                    elem['date'] = elem['date'].rstrip()

                    # print elem['date']

                    ts = time.mktime(datetime.datetime.strptime(elem['date'], "%B %d %Y").timetuple())

                    items[str(int(ts)+num)] = elem

    # return items

    collection = []
    for key in sorted(items, reverse=True):
        collection.append(items[key])

    return collection