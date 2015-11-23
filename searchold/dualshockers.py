#!/bin/python

import re

def parse(soup, res):
    news = soup.findAll('div')

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            if 'entry' in classes:
                elem = {}

                title = item.h2.a.string

                desc = ''
                for val in list(item.div.p.contents):
                    try:
                        desc += val.string
                    except TypeError:
                        print 'error'

                link = item.h2.a.get('href')
                date = '-'

                # set item object
                elem['title'] = title
                elem['desc'] = desc
                elem['link'] = link
                elem['date'] = date

                # serarch for specific items
                searchTitle = re.search( r'(Final Fantasy|Square Enix)', title, re.M|re.I)
                searchDesc = re.search( r'(Final Fantasy|Square Enix)', desc, re.M|re.I)

                if searchTitle or searchDesc:
                    items.append(elem)
                    print elem['title']
                else:
                    # print "Nothing found!!"
                    pass
                

                # print elem['title']

    return items
