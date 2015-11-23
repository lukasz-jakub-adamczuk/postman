#!/bin/python

def parse(soup, res):
    news = soup.findAll('td')

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            for c in classes:
                if c == 'details':
                    elem = {}

                    # old
                    desc = ''
                    # if item.section.p is not None:
                        # desc = item.section.p.string

                    elem['title'] = item.div.findNextSibling('div').a.string
                    elem['desc'] = desc
                    elem['link'] = item.div.findNextSibling('div').a.get('href')
                    elem['date'] = item.div.findNextSibling('div').findNextSibling('div').contents[0].replace('Published ', '').replace('.', '')

                    # new
                    desc = ''
                    # if item.div.findNextSibling('div').p is not None:
                    #     desc = item.div.findNextSibling('div').p.string

                    # elem['title'] = item.header.h1.a.string
                    # elem['desc'] = desc
                    # elem['link'] = item.header.h1.a.get('href')
                    # elem['date'] = elem['link'][24:34]

                    items.append(elem)

    return items