#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import urllib


def replacer( l ):
    l = l.replace('&#8220;','“').replace('&#8221;','”').replace(':',' ').replace('<small>','').replace('</small>','').replace('<i>','').replace('</i>','').replace('<sup>','').replace('</sup>','').replace('-',' ').replace('&#8212;',"—").replace('&#8216;',"‘").replace('&#8217;',"’").replace('&#239;','ï').replace('&#246;','ö').replace('&#126;','~').replace('&#8211;','–').replace('&#038;','&').rstrip()    
    return l


res = urllib.urlopen("http://icml.cc/2016/?page_id=1649")

pdf = ""
ti = []
aus = []
abs = []

for l in res.readlines():
    if '<li><span class="titlepaper"><a href="#">' in l:
        title = l.split('<li><span class="titlepaper"><a href="#">')[1].split('</a>')[0]
        title = replacer(title)
        ti.append(title)
        
    if '<span class="authors">' in l:
        authors = l.split('<span class="authors">')[1].split('</span>')[0]
        authors = authors.replace('<i>',',').replace('</i>',',')
        authors = replacer(authors)
        aus.append(authors)
        
    if '<div class="abstract">' in l:
        abst = l.split('<div class="abstract">')[1].split('</div>')[0]
        abs.append(replacer(abst))

for i in xrange(len(ti)):
    
    url = 'http://export.arxiv.org/api/query?search_query=all:'+ti[i]+'&start=0&max_results=10'
    out = 0
    u = urllib.urlopen(url)
    l_title = 'abcde'
    for l in u.readlines():
        if '<title>' in l:
            l_title = replacer(l).split('<title>')[1].split('</title>')[0]
        if '<link title="pdf"' in l:
            pdf = l.split('"')[3]

        if l_title.lower() in ti[i].lower():
            out = 1
            break
    u.close()
    if out == 0:
        pdf = "Not Found in ArXiv"
        
    print pdf+"\t"+ti[i]+"\t"+aus[i]+"\t"+abs[i]



        
