#!/bin/python

def parse(soup, res):
    news = soup.findAll('div')

    items = []
    for item in news:
        if hasattr(item, 'get') and item.get('class') == 'sl-item':
            elem = {}
            if item.div.b.string == 'Ad':
                pass
            else:
                elem['title'] = item.contents[3].h1.a.string
                elem['desc'] = item.contents[3].div.contents[2]
                elem['link'] = res['host'] + item.contents[3].ul.contents[5].a['href']
                elem['date'] = item.contents[3].div.b.string.replace('  -', '')

                items.append(elem)

    return items
