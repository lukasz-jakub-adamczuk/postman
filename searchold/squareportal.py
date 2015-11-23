#!/bin/python

def parse(soup, res):
    news = soup.findAll('article')

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')

            if 'post' in classes and 'cover' in classes:
                elem = {}

                # old
                # desc = ''
                # if item.div.p is not None:
                #     desc = item.div.p.string

                # elem['title'] = item.div.div.div.div.h1.a.string
                # elem['desc'] = ''
                # elem['link'] = item.div.div.div.div.h1.a.get('href')
                # elem['date'] = ''

                # items.append(elem)
            else:
                if 'post' in classes:
                    elem = {}

                    # old
                    desc = ''
                    if item.section.p is not None:
                        desc = item.section.p.string

                    elem['title'] = item.section.h2.a.string
                    elem['link'] = item.section.h2.a.get('href')
                    elem['date'] = item.section.div.span.findNextSibling('a').time.string
                    elem['desc'] = desc

                    # print item

                    print elem['title'].replace(u'\u2012', '-').replace(u'\u2013', '-').replace(u'\u2014', '-').strip()
                    
                    items.append(elem)

    return items