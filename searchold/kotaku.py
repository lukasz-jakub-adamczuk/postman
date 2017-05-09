#!/bin/python

def parse(soup, res):
    news = soup.findAll('div')

    # print len(news)
    # print soup

    items = []
    for item in news:
        if item.get('class') != None:
            classes = item['class'].split(' ')
            # print classes
            for c in classes:
                if c == 'post-wrapper':
                # if c == 'first-text':
                    elem = {}

                    # print item

                    if not item.article.header:
                        pass
                    else:
                        title = ''
                        for val in list(item.article.header.h1.a.contents):
                            title += val.string

                        desc = ''

                        link = item.article.header.h1.a.get('href')
                        date = ''

                        summary = item.article.div.findNextSibling('div')
                        if 'marquee-asset' in summary.get('class').split(' '):
                            summary = summary.findNextSibling('div')

                        # print item.article.header.time
                        date = item.article.header.time.get('datetime').replace('T', ' ')[0:19]
                        
                        if summary:
                            # print summary
                            try:
                                for val in list(summary.div.p.contents):
                                    if hasattr(val, 'get'):
                                        if val.get('class') is not None:
                                            if 'read-more' in val.get('class'):
                                                # print val
                                                # try:
                                                #     date = val.span.span.a.span.string
                                                # except AttributeError:
                                                #     pass
                                                pass
                                        else:
                                            for v in list(val.contents):
                                                if v.string is not None:
                                                # print type(v)
                                                    desc += v.string
                                                # print v.string
                                    else:
                                        desc += val.string
                            except AttributeError:
                                pass

                            elem['title'] = title
                            elem['desc'] = desc
                            elem['link'] = link
                            elem['date'] = date

                        items.append(elem)

                        try:
                            print title
                        except UnicodeEncodeError:
                            pass

    return items