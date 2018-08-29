from Maltego2 import *
import requests, json
from Mylogging import logging

def trx_basesearch(m):
    limit=m.slider
    url="https://api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=PerformSearch&format=json&query=dccreator:"
    TRX = MaltegoTransform()
    
    author = m.getProperty("person.fullname").strip()

    r=requests.get(url+'"'+author+'"'+"&hits="+str(limit))
#    import pprint
#    pprint.pprint(r.json())

    for doc in r.json()['response']['docs']:
        try:
            new= TRX.addEntity("me.Article", doc['dctitle'])
        except:
#            print('No title')
            continue

        try:
            new.addProperty("year","Year", 'strict', str(doc['dcyear']))
        except:
            pass

        link=doc['dclink']
        new.addDisplayInformation('<a href="'+link+'"> '+link+' </a>','Link to file')

        try:
            author=doc['dccreator']
        except:
#            print 'no author'
            pass
        else:
            if type(author) is list:
                authors='; '.join(o for o in author)
                new.addProperty("author","Author","strict",authors)
#                print 'author is list'
            elif type(author) is unicode:
                new.addProperty("author","Author","strict",author)
#                print 'author is one'
        try:
            new.addProperty("abstract","Abstract","strict",doc['dcdescription'])
        except:
            pass


    logging(TRX.returnOutput(),m.Maltegoxml)

    return TRX.returnOutput()



