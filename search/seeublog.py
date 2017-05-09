#!/bin/python

def parse(soup, res):
    news = soup.find_all('div', class_='node-blogs')

    i = 1
    items = []
    for item in news:
        elem = {}
        elem['title'] = 'title'
        elem['desc'] = 'description'
        elem['link'] = 'link'
        elem['date'] = 'date'

        date = item.div.div.contents[2]
        pos = date.index('on ')+3

        desc = ''
        for val in list(item.div.find_next_sibling('div').find_next_sibling('div').contents):
            if val.name == 'p':
                for v in list(val.contents):
                    if v.string != None:
                        desc += v.string
        
        elem['title'] = item.div.h2.a.string.strip()
        elem['desc'] = desc
        elem['link'] = res['host'] + '/us/' + item.div.h2.a.get('href')
        elem['date'] = date[pos:]

        items.append(elem)

        print (str(i)+'. ').ljust(4) + elem['title']
        i += 1

    return items
