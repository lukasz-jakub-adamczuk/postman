#!/bin/python

def parse(soup, res):
    # news = soup.findAll('td')
    news = soup.select('.type-post')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}
        
        elem['title']   = item.div.div.findNextSibling('div').h3.a.string.strip()
        elem['link']    = item.div.div.findNextSibling('div').h3.a.get('href')
        elem['date']    = item.div.div.findNextSibling('div').span.findNextSibling('span').span.contents[1]
        
        try:
            for val in list(item.div.div.findNextSibling('div').span.contents):
                try:
                    elem['tags'].append(val.string)
                except TypeError:
                    pass
        except AttributeError:
            pass
        
        elem['img']   = item.div.div.div.span.get('style').replace('background-image: url(\'', '').replace('\')', '')
        
        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1

    return items