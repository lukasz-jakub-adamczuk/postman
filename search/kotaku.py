#!/bin/python

def parse(soup, res):
    news = soup.find_all('article', class_='js_post_item')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}
        
        header = item.div.findNextSibling('div').findNextSibling('div').figure.findNextSibling('div').div.findNextSibling('div').a.h2
        
        if header != None:
            for val in list(header.contents):
                try:
                    elem['title'] += val.string
                except TypeError:
                    pass
        
        try:
            elem['img'] = item.div.findNextSibling('div').findNextSibling('div').figure.a.div.div.img.get('srcset').split(' ')[0]
        except AttributeError:
            pass

        elem['link'] = item.div.findNextSibling('div').findNextSibling('div').figure.a.get('href')
        
        summary = ''
        summary = item.div.findNextSibling('div').findNextSibling('div').figure.next_sibling.div.p
        if summary != None:
            for val in list(summary.contents):
                try:
                    elem['desc'] += val.string
                except TypeError:
                    pass
        
        elem['date'] = item.div.div.span.findNextSibling('div').string


        try:
            category = item.div.findNextSibling('div').findNextSibling('div').figure.findNextSibling('div').div.div.div.span.a.span.string
            print(category)
            elem['tag'].append(category)
        except AttributeError:
            pass
        print(elem['tag'])

        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1
    return items