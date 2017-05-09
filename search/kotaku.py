#!/bin/python

def parse(soup, res):
    news = soup.find_all('div', class_='post-wrapper')

    items = []
    for item in news:
        if item.get('class') != None:
            # print item['class']
            # classes = item['class'].split(' ')
            classes = item['class']
            # print classes
            for c in classes:
                if c == 'post-wrapper':
                # if c == 'first-text':
                    elem = {}

                    if not item.article.header:
                        pass
                    else:
                        title = ''
                        desc = ''
                        link = ''
                        date = ''

                        # print item.article.header.h1.a.contents
                        for val in list(item.article.header.h1.a.contents):
                            try:
                                title += val.string
                            except TypeError:
                                pass

                        link = item.article.header.h1.a.get('href')
                        summary = item.article.div.findNextSibling('div')
                        # summary = item.find_all('div', class_='entry-summary')

                        # if 'marquee-asset' in summary.get('class'):
                            # summary = summary.findNextSibling('div')
                            # print 'marquee-asset'
                            # summary = item.find_all('div', class_='entry-summary')
                        
                        date = item.article.header.div.div.time.a.string    
                        
                        if summary:
                            # print summary.div.p
                            for val in list(summary.p.contents):
                                if hasattr(val, 'get'):
                                    if val.get('class') is not None:
                                        if 'read-more' in val.get('class'):
                                            # date = val.span.span.a.span.string
                                            pass
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
                            elem['link'] = link
                            elem['date'] = date

                        items.append(elem)

                        print elem['title']
    return items