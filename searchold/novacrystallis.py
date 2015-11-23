#!/bin/python

def parse(soup, res):
    news = soup.findAll('div')

    # print len(news)
    # print 'soup in 
    # print soup

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            for c in classes:
                if c == 'news_block':
                    elem = {}

                    # print item
                    # print item.a
                    # print item.a.findNextSibling('a')

                    title = ''
                    for val in list(item.a.findNextSibling('a').span.contents):
                        title += val.string

                    desc = ''
                    desc = item.a.findNextSibling('div').findNextSibling('div').findNextSibling('div').string

                    elem['title'] = title
                    elem['desc'] = desc
                    elem['link'] = item.a.get('href')
                    elem['date'] = item.a.findNextSibling('div').a.findNextSibling('span').string

                    items.append(elem)

    return items