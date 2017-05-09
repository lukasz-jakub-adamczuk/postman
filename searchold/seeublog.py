#!/bin/python

def parse(soup, res):
    news = soup.findAll('div')

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            for c in classes:
                if c == 'node-blogs':
                    elem = {}

                    date = item.div.div.contents[2]
                    pos = date.index('on ')+3

                    desc = ''
                    for val in list(item.div.findNextSibling('div').findNextSibling('div').contents):
                        # print str(val)[0:3]
                        if str(val)[0:2] == '<p':
                            for v in list(val.contents):
                                if v.string != None:
                                    desc += v.string
                    
                    elem['title'] = item.div.h2.a.string
                    elem['desc'] = desc
                    elem['link'] = res['host'] + res['url'].replace('blog', '') + item.div.h2.a.get('href')
                    elem['date'] = date[pos:]

                    print elem['title']

                    items.append(elem)

    return items