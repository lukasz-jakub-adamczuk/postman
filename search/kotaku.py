#!/bin/python

def parse(soup, res):
    news = soup.find_all('div', class_='post-wrapper')

    items = []
    for item in news:
        elem = {}
        if not item.article.header:
            pass
        else:
            title = ''
            for val in list(item.article.header.h1.a.contents):
                title += val.string

            desc = ''
            for val in list(item.article.div.find_next_sibling('div').div.p.contents):
                if hasattr(val, 'get'):
                    if val.get('class') is not None:
                        if 'read-more' in val.get('class'):
                            date = val.span.span.a.span.string
                            # pass
                    else:
                        for v in list(val.contents):
                            desc += v.string
                else:
                    desc += val.string

            elem['title'] = title
            elem['desc'] = desc
            elem['link'] = item.article.header.h1.a.get('href')
            elem['date'] = date            

            items.append(elem)

    return items