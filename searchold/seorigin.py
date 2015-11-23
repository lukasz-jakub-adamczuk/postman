#!/bin/python

import time, datetime

def parse(soup, res):
    news = soup.findAll('div')

    # marker to make news unique by timestamp
    num = 0

    items = {}
    for item in news:
        if hasattr(item, 'get') and item.get('class') != None:
            classes = item['class'].split(' ')
            for c in classes:
                # latest news
                if c == 'slider':
                    num = 0
                    for slide in item.ul.contents:
                        if str(slide)[0:3] == '<li':
                            elem = {}

                            elem['title'] = slide.div.h3.a.string
                            elem['desc'] = '...'
                            elem['link'] = slide.div.h3.a.get('href')
                            elem['date'] = slide.div.time.string
                            
                            ts = time.mktime(datetime.datetime.strptime(elem['date'], "%B %d, %Y").timetuple())

                            items[str(int(ts)+num)] = elem
                            num += 1
                # latest news
                if c == 'post':
                    elem = {}

                    elem['title'] = item.h2.a.string
                    elem['desc'] = '...'
                    elem['link'] = item.h2.a.get('href')
                    elem['date'] = item.div.time.string

                    # print elem['title']

                    ts = time.mktime(datetime.datetime.strptime(elem['date'].rstrip(), "%B %d, %Y").timetuple())

                    # print ts

                    items[str(int(ts)+num)] = elem
                # kh news
                # if c == 'blog-carousel':
                #     for i in item.div.contents:
                #         if str(i)[0:8] == '<article':
                #             elem = {}

                #             elem['title'] = i.div.h2.a.string
                #             elem['desc'] = '...'
                #             elem['link'] = i.div.h2.a.get('href')
                #             elem['date'] = i.div.time.string

                #             ts = time.mktime(datetime.datetime.strptime(elem['date'], "%B %d, %Y").timetuple())
                            
                #             items[str(int(ts)+num)] = elem

    # print items

    collection = []
    for key in sorted(items, reverse=True):
        collection.append(items[key])

    return collection
