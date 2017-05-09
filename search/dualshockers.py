#!/bin/python

import re

def parse(soup, res):
    # news = soup.findAll('div')
    news = soup.select('.post-inner')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': ''}
        
        desc = ''
        for val in list(item.find('p').contents):
            try:
                if val.string is not None:
                    desc += val.string
            except TypeError:
                pass

        elem['title'] = item.find('h2').a.string
        elem['desc'] = desc.replace('...Read More', '')
        elem['link'] = item.find('h2').a.get('href')
        elem['date'] = item.find('span', class_='date').span.contents[1]

        # search for specific items
        searchTitle = re.search( r'(Final Fantasy|Square Enix)', elem['title'], re.M|re.I)
        searchDesc = re.search( r'(Final Fantasy|Square Enix)', elem['desc'], re.M|re.I)

        if searchTitle or searchDesc:
            items.append(elem)
            
            print (str(i)+'. ').ljust(4) + elem['title']
            i += 1
        else:
            pass

    return items
