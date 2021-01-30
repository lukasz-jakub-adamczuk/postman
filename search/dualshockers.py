#!/bin/python

import re

def parse(soup, res):
    # news = soup.findAll('div')
    news = soup.select('article.article')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}
        
        # desc = ''
        # for val in list(item.find('h5').contents):
        #     try:
        #         if val.string is not None:
        #             desc += val.string
        #     except TypeError:
        #         pass

        # print(desc)
        elem['title'] = item.find('h4').a.string
        # elem['desc'] = desc.replace('...Read More', '')
        elem['link'] = item.find('h4').a.get('href')
        elem['img'] = item.div.a.img.get('src')
        # print(item.div.findNextSibling('div').a.string)
        # elem['date'] = item.find('time').span.contents[0]
        try:
            elem['tags'].append(item.div.findNextSibling('div').a.string)
            elem['date'] = item.time.contents[0]
        except AttributeError:
            pass

        # search for specific items
        searchTitle = re.search( r'(Final Fantasy|Square Enix)', elem['title'], re.M|re.I)
        searchDesc = re.search( r'(Final Fantasy|Square Enix)', elem['desc'], re.M|re.I)

        # if True:
        if searchTitle:# or searchDesc:
            items.append(elem)
            
            print((str(i)+'. ').ljust(4) + elem['title'])
            i += 1
        else:
            pass

    return items
