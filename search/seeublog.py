#!/bin/python

def parse(soup, res):
    news = soup.find_all('div', class_='cell')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}

        # date = item.div.div.contents[2]
        # pos = date.index('on ')+3

        try:
            elem['title'] = item.div.findNextSibling('div').div.span.string.strip()
        except AttributeError:
            pass
        
        try:
            elem['title'] = item.div.findNextSibling('div').h2.a.string.strip()
        except AttributeError:
            pass

        elem['link'] = item.div.div.a.get('href')

        try:
            elem['tags'].append(item.div.findNextSibling('div').div.div.div.string.strip())
        except AttributeError:
            pass

        try:
            elem['desc'] = item.div.findNextSibling('div').h2.findNextSibling('div').span.p.string.strip()
        except AttributeError:
            pass

        
        elem['img'] = item.div.div.get('style').replace('background-image: url(', '').replace('?quality=65);', '')
        
        elem['link'] = res['host'] + item.div.div.a.get('href')
        
        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1

    return items
