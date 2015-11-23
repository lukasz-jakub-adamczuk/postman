#!/bin/python

def parse(soup, res):
    news = soup.findAll('div')

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            for c in classes:
                if c == 'post-wrapper':
                    elem = {}

                    if not item.article.header:
                        pass
                    else:
                        title = ''
                        for val in list(item.article.header.h1.a.contents):
                            title += val.string

                        desc = ''
                        summary = item.article.div.findNextSibling('div')
                        if 'marquee-asset' in summary.get('class').split(' '):
                            summary = summary.findNextSibling('div')
                        
                        for val in list(summary.div.p.contents):
                            if hasattr(val, 'get'):
                                if val.get('class') is not None:
                                    if 'read-more' in val.get('class'):
                                        date = val.span.span.a.span.string
                                        # pass
                                else:
                                    for v in list(val.contents):
                                        if v.string is not None:
                                        # print type(v)
                                            desc += v.string
                                        # print v.string
                            else:
                                desc += val.string

                        elem['title'] = title
                        elem['desc'] = desc
                        elem['link'] = item.article.header.h1.a.get('href')
                        elem['date'] = date

                        items.append(elem)

                        print title

    return items