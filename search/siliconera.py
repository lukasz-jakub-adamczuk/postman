#!/bin/python

def parse(soup, res):
    news = soup.find_all('article', class_='post')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}

        elem['title']   = item.div.findNextSibling('div').h3.a.string
        elem['link']    = item.div.findNextSibling('div').h3.a.get('href')
        elem['desc']    = item.div.findNextSibling('div').div.div.string
        elem['date']    = item.time.contents[1]
        elem['tags']    = []
        elem['img']     = item.div.a.img.get('src')

        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1

    return items