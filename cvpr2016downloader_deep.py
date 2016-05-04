#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import urllib
res = urllib.urlopen("http://cvpr2016.thecvf.com/program/main_conference")
might_be_CVPR = 1

for l in [ line  for line in res.readlines() if '<strong>' in line ]:
    if not '<a' in l:
        title = l.split('<strong>')[1].split(';')[0].split('</strong>')[0].replace('&#8220','“').replace('&#8221','”').replace(':',' ')
        
        url = 'http://export.arxiv.org/api/query?search_query=all:'+title+'&start=0&max_results=1'
    try:

        authors = []
        pdf = ""
        deep = 0
        abses=[]
        
        for l in urllib.urlopen(url).readlines():
            if '<published>' in l:
                ll=l.split('</published>')[0]
                lll=ll.split('-')
                if int(lll[0].replace('<published>','')) < 2015 or ( int(lll[0].replace('<published>','')) > 2015 and int(lll[1]) < 10 ):
                    might_be_CVPR = 0

            if '</arxiv:comment>' in l:
                if 'CVPR' in l and '2016' in l:
                    might_be_CVPR = 1

                    
            if '<link title="pdf"' in l:
                pdf = l.split('"')[3]
            if '<name>' in l:
                authors.append(l)
            if '<summary>' in l or sum == 1:
                sum = 1
                if 'deep' in l:
                    deep = 1
                elif 'Eeep' in l:
                    deep = 1
                elif 'neural' in l:
                    deep = 1
                elif 'Neural' in l:
                    deep = 1
                elif 'convolutional' in l:
                    deep = 1
                elif 'Convolutional' in l:
                    deep = 1
                elif 'recurrent' in l:
                    deep = 1
                elif 'Recurrent' in l:
                    deep = 1
                elif 'LSTM' in l:
                    deep = 1
                elif 'Long Short' in l:
                    deep = 1
                elif 'network' in l:
                    deep = 1
                elif 'Network' in l:
                    deep = 1

                if deep == 1:
                    abses.append(l)
                    
            if '</summary>' in l:
                sum = 0
                
        aus = ""
        abs = ""
        for author in authors:
            aus += (author.split('<name>')[1].split('</name>')[0].rstrip())+","
        for ab in abses:
            ab = ab.replace('<summary>',"")
            ab = ab.replace('</summary>',"")
            abs += ab.rstrip()
            
    except IndexError:
        pdf = "Not Found in ArXiv"
        aus = ""
        deep = 0
        abs = ""

    if might_be_CVPR == 0:
        pdf = "Not Found in ArXiv"
        
    if deep == 1:
        print pdf+"\t"+title+"\t"+aus+"\t"+abs

might_be_CVPR = 1



        

