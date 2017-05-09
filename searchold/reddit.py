#!/bin/python

def parse(soup, res):
    news = soup.findAll('div')

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            if 'thing' in classes:
                elem = {}

                # title = ''
                # for val in list(item.h2.a.contents):
                #     title += val

                link = item.div.findNextSibling('div').p.a.get('href')
                if link[0:4] != 'http':
                    link = 'https://www.reddit.com' + link
                
                elem['title'] = item.div.findNextSibling('div').p.a.string
                elem['desc'] = ''
                elem['link'] = link
                elem['date'] = item.div.findNextSibling('div').p.findNextSibling('p').time.string

                items.append(elem)

                print elem['title']

    return items
