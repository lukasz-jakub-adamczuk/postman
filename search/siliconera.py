#!/bin/python

def parse(soup, res):
    news = soup.find_all('div', class_='post')

    items = []
    for item in news:
        elem = {}

        date = item.small.string
        pos = date.index('.')+2
        
        elem['title'] = item.h2.a.string
        elem['desc'] = item.p.find_next_sibling('p').string
        elem['link'] = item.h2.a.get('href')
        elem['date'] = date[pos:]

        items.append(elem)

    return items