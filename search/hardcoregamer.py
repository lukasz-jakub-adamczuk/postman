#!/bin/python

def parse(soup, res):
    news = soup.find_all('article', class_='post')

    i = 1
    items = []
    for item in news:
        elem = {'title': '', 'link': '', 'desc': '', 'date': '', 'tags': [], 'img': ''}
        
        elem['title'] = item.div.h1.a.string
        elem['link'] = item.div.h1.a.get('href')
        elem['img']     = item.div.a.img.get('srcset').split(' ')[0]
        # print(elem['img'])

        elem['date'] = elem['link'][26:36]
        
        try:
            # print(item.div.findNextSibling('div').div.ul.contents)
            # print(list(item.div.findNextSibling('div').div.ul.contents))
            elem['tags'].append(item.div.findNextSibling('div').div.ul.li.a.string)
            # for val in list(item.div.findNextSibling('div').div.ul.contents):
            #     try:
            #         print('value...')
            #         print('...' + val.li.a.string)
            #         elem['tags'].append(val.li.a.string)
                    
            #     except TypeError:
            #         pass
        except AttributeError:
            pass

        # print(item.div.findNextSibling('div').div.ul.contents)

        items.append(elem)

        print((str(i)+'. ').ljust(4) + elem['title'])
        i += 1

    return items