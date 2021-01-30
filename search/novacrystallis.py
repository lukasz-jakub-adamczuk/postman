#!/bin/python

def parse(soup, res):
    # news = soup.findAll('div')
    news = soup.select('.post')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}

        elem['title']   = item.div.findNextSibling('div').div.a.string
        elem['link']    = item.div.findNextSibling('div').div.a.get('href')
        elem['desc']    = item.div.findNextSibling('div').div.findNextSibling('div').string
        elem['date']    = item.div.a.div.div.string
        elem['img']     = item.div.a.img.get('data-ezsrc')

        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1

    return items