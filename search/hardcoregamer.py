#!/bin/python

def parse(soup, res):
    news = soup.find_all('div', class_='post_inner_wrapper')

    items = []
    for item in news:
        elem = {}

        desc = ''
        for val in list(item.p.contents):
            desc += val.string

        date = item.div.div.find_next_sibling('div').string
        pos = date.index('on ')+3
        
        elem['title'] = item.div.div.h3.a.string
        elem['desc'] = desc
        elem['link'] = item.div.div.h3.a.get('href')
        elem['date'] = date[pos:]

        items.append(elem)

    return items