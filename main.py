#!/bin/python

import os, sys
import time, datetime

# import urllib2
import requests

import yaml
import json
from BeautifulSoup import BeautifulSoup
# from bs4 import BeautifulSoup

import HTMLParser

# import searchold
from searchold import n4g
from searchold import kotaku
from searchold import squareportal
from searchold import hardcoregamer
from searchold import vgleaks
from searchold import siliconera
from searchold import seeublog
from searchold import seorigin
from searchold import gematsu
from searchold import novacrystallis
from searchold import reddit
from searchold import dualshockers

# from search import n4g
# from search import kotaku
# from search import squareportal
# from search import hardcoregamer
# from search import vgleaks
# from search import siliconera
# from search import seeublog
# from search import seorigin

# functions
def parseArgs(args):
    options = {}
    for param in args:
        if len(param) > 2:
            if param[0:2] == '--':
                pos = param.index('=')
                key = param[2:pos]
                val = param[pos+1:]
                if val == 'false' or val == 'true':
                    val = bool()
                options[key] = val
    return options

def slice_source(content, begin, end):
    start = content.index(begin)
    stop = content.index(end, start)
    return content[start:stop]

def cut_source_code(content, name):
    if name == 'seeublog':
        return slice_source(content, '<div id="main-content"', '<div id="sidebar-right"')
    if name == 'kotaku':
        return slice_source(content, '<div class="post-list', '<div class="row load-more">')
    if name == 'n4g':
        return slice_source(content, '<div class="storylist-update">', '<!--%: Ads')
    if name == 'siliconera':
        return slice_source(content, '<div class="leftcontainer">', '<div class="rightcontainer">')
    if name == 'vgleaks':
        return slice_source(content, '<div id="blog-item-holder"', '<div class="gdl-pagination">')
    if name == 'squareportal':
        return slice_source(content, '<div id="main-content">', '<div class="sidebar sidebar-category-summaries">')
    if name == 'hardcoregamer':
        return slice_source(content, '<section id="primary"', '<div id="secondary"')
    if name == 'gematsu':
        return slice_source(content, '<div id="content">', '<div id="sidebar">')
    if name == 'novacrystallis':
        return slice_source(content, '<div id="index_section_2_left_box">', '<div id="index_section_2_right">')
    if name == 'reddit':
        return slice_source(content, '<div id="siteTable"', '<div class="footer-parent">')
    return content


# main code
if len(sys.argv) < 2:
    print 'Not enough arguments'
    sys.exit(1)
else:
    options = parseArgs(sys.argv)

env = 'dev'
if 'env' in options:
    env = options['env']
if 'page' in options:
    page = options['page']

path = os.path.dirname(os.path.realpath(__file__))
# print path

input = open(path + '/conf.yml', 'r')
conf = yaml.load(input)
input.close()

dispatcher = {
    'n4g': n4g.parse,
    'kotaku': kotaku.parse,
    'squareportal': squareportal.parse,
    'hardcoregamer': hardcoregamer.parse,
    'vgleaks': vgleaks.parse,
    'siliconera': siliconera.parse,
    'seeublog': seeublog.parse,
    'senablog': seeublog.parse,
    'seorigin': seorigin.parse,
    'gematsu': gematsu.parse,
    'novacrystallis': novacrystallis.parse,
    'reddit': reddit.parse,
    'dualshockers': dualshockers.parse
}

# place for feeds
path += '/feeds'

if (os.path.exists(path) == False):
    os.makedirs(path)

if page in conf:
    res = conf[page]

    url = res['host']
    if res['url'] != None:
        url += res['url']

    header = 'Searching news for ' + url
    print header
    print ''.ljust(len(header), '-')
    # print '  Title: ' + soup.title.string.strip()
    # try:
    #     response = urllib2.urlopen(url)
    # except urllib2.HTTPError:
    #     print '...urllib2.HTTPError...but get from file...'
        
    #     input = open('pages/' + res['name'], 'r')
    #     response = input.read()
    #     input.close()

    # try:
    #     soup = BeautifulSoup(response)
    # except HTMLParser.HTMLParseError:        
    #     input = open('pages/' + res['name'], 'r')
    #     response = input.read()
    #     input.close()

    #     soup = BeautifulSoup(response)

    # new way
    response = requests.get(url)

    # python 2.6 need partial response
    source = cut_source_code(response.content, res['func'])
    # print source[0:500]

    # crazy hack for broken source on novacrystallis
    source = source.replace('week\'s "feedback special"', '')
    # print source[0:500]
    
    soup = BeautifulSoup(source)
    # print soup
    
    # python 2.7 has better parser and handle full response
    # soup = BeautifulSoup(response.content)

    filename = path + '/' + page + '.json'
    
    # try:
    items = dispatcher[res['func']](soup, res)

    footer = 'Found: ' + str(len(items)) + ' items'
    print
    print footer
    # print ''.ljust(len(footer), '-')
    print 

    feed =  json.dumps(items)

    # except AttributeError as err:
    #     print 'AttributeError ({0}): {1}'.format(err.errno, err.strerror)
    #     feed = '[]'
    # except ValueError as err:
    #     print 'ValuesError ({0}): {1}'.format(err.errno, err.strerror)
    #     feed = '[]'
    
    # except Exception as inst:
    #     print type(inst)     # the exception instance
    #     print inst.args      # arguments stored in .args
    #     print inst 
    #     feed = '[]'

    input = open(filename, 'w')
    input.write(feed)
    input.close()


    