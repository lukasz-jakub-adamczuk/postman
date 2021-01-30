#!/bin/python

def parse(soup, res):
    print(soup)
    # news = soup.findAll('div')
    news = soup.find_all('div', class_='thing')

    i = 1
    items = []
    for item in news:
        # print(item)
        elem = {}

                # title = ''
                # for val in list(item.h2.a.contents):
                #     title += val

        link = item.div.findNextSibling('div').p.a.get('href')
        if link[0:4] != 'http':
            link = 'https://www.reddit.com' + link
        
        elem['title'] = item.div.findNextSibling('div').p.a.string
        elem['desc'] = ''
        elem['link'] = link
        elem['date'] = item.div.findNextSibling('div').p.findNextSibling('p').time.string

        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1

    return items
