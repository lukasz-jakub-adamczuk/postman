#!/bin/python

def parse(soup, res):
    # news = soup.findAll('div')
    news = soup.select('.news_block')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': ''}
        
        title = ''
        for val in list(item.a.findNextSibling('a').span.contents):
            title += val.string

        desc = ''
        desc = item.a.findNextSibling('div').findNextSibling('div').findNextSibling('div').string

        elem['title'] = title
        elem['desc'] = desc
        elem['link'] = item.a.get('href')
        elem['date'] = item.a.findNextSibling('div').a.findNextSibling('span').string

        items.append(elem)

        print (str(i)+'. ').ljust(4) + elem['title']
        i += 1

    return items