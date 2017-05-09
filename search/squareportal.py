#!/bin/python

def parse(soup, res):
    news = soup.find_all('article', class_='post')

    items = []
    for item in news:
        elem = {}

        elem['title'] = item.section.h2.a.string.strip()
        if item.section.p != None:
            elem['desc'] = item.section.p.string
        elem['link'] = item.section.h2.a.get('href')
        elem['date'] = item.section.div.time.string

        items.append(elem)

        print elem['title']

    return items