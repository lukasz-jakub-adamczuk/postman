#!/bin/python

def parse(soup, res):
    # news = soup.findAll('td')
    news = soup.select('.details')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': ''}

        elem['title'] = item.div.findNextSibling('div').a.string
        elem['link'] = item.div.findNextSibling('div').a.get('href')
        elem['date'] = item.div.findNextSibling('div').findNextSibling('div').contents[0].replace('Published ', '').replace('.', '')

        items.append(elem)

        print (str(i)+'. ').ljust(4) + elem['title']
        i += 1

    return items