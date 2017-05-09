#!/bin/python

def parse(soup, res):
    # news = soup.find_all('div', class_='f-item')
    news = soup.select('.f-item > .si-wrap')

    i = 1
    items = []
    for item in news:
        elem = {}

        elem['title'] = item.div.find_next_sibling('div').a.h2.string
        elem['desc'] = '...'
        elem['link'] = item.div.find_next_sibling('div').a['href']
        elem['date'] = item.div.find_next_sibling('div').div.div.contents[0]

        if elem['link'][0] == '/':
            elem['link'] = res['host'] + elem['link']
        
        items.append(elem)

        print (str(i)+'. ').ljust(4) + elem['title']
        i += 1
        
    return items
