#!/bin/python

def parse(soup, res):
    news = soup.find_all('div', class_='blog-context-wrapper')

    items = []
    for item in news:
        elem = {}

        title = ''
        for val in list(item.h2.a.contents):
            title += val
        
        elem['title'] = title
        elem['desc'] = item.div.find_next_sibling('div').contents[0]
        elem['link'] = item.h2.a.get('href')
        elem['date'] = item.div.div.a.string

        items.append(elem)

    return items
