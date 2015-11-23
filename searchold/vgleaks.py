#!/bin/python

def parse(soup, res):
    news = soup.findAll('div')

    items = []
    for item in news:
        if item.get('class') != None:
            if item['class'] == 'blog-context-wrapper':
                elem = {}

                title = ''
                for val in list(item.h2.a.contents):
                    title += val
                
                elem['title'] = title
                elem['desc'] = item.div.findNextSibling('div').contents[0]
                elem['link'] = item.h2.a.get('href')
                elem['date'] = item.div.div.a.string

                items.append(elem)

    return items
