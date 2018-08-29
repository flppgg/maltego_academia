from Mylogging import logging
import requests, json
from Maltego2 import *

def trx_searchtitle(m):
    
    TRX = MaltegoTransform()
    #me.parseArguments(sys.argv)
    title=m.getProperty("title.article")


    url = 'http://api.crossref.org/works?query='

    r= requests.get(url+title+'&rows=1')

    titler = r.json()['message']['items'][0]['title'][0]
    doi = r.json()['message']['items'][0]['DOI']
    URL = r.json()['message']['items'][0]['URL']

    try:
        year = str(r.json()['message']['items'][0]['published-print'])
    except:
        try:
            year = str(r.json()['message']['items'][0]['published-online']['date-parts'])
        except:
            year = str(r.json()['message']['items'][0]['created']['date-parts'])
    year = year.translate(None, "{}abcdefghijklmnopqrstuvz':[]-,")

    try:
        u = r.json()['message']['items'][0]['author']
        authori = []
        for i in u:
            authore = i['family'].encode('utf-8')+' '+i['given'].encode('utf-8')+'; '
            authori.append(authore)
    except:
        authori = []
        authori.append(r.json()['message']['items'][0]['publisher'])



    new = TRX.addEntity("me.Article", title)
    new.addProperty("DOI","DOI", 'strict', str(doi))
    new.addDisplayInformation('<a href="%s"> click here to go to the webpage </a>' %URL, 'DOI URL')
    new.addProperty("url","url", 'strict', str(URL))
    new.addProperty("year","Year", 'strict', str(year))
    new.addProperty("author","Author", 'loose', ''.join(authori))
    new.setValue(titler.encode('utf-8')) #what the hell is this???????????????????

    logging(TRX.returnOutput(),m.Maltegoxml)

    return TRX.returnOutput()

