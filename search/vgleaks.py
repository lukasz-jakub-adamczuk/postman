#!/bin/python

def parse(soup, res):
    print(soup)
    news = soup.find_all('article', class_='post')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}

        title = ''
        for val in list(item.div.find_next_sibling('div').header.h3.a.contents):
            title += val
        
        elem['title'] = title
        # elem['desc'] = item.div.find_next_sibling('div').contents[0]
        # elem['link'] = item.h2.a.get('href')
        # elem['date'] = item.div.div.a.string

        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1

    return items
