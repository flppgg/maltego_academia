from Maltego2 import *
import requests
import xml.etree.ElementTree as ET
from Mylogging import logging


def trx_cermine(m):

    TRX=MaltegoTransform()

    path=str(m.getProperty('article.path'))
    print path
    data=open(path.replace('"',''),'rb').read()
    url='http://cermine.ceon.pl/extract.do'
    headers={'Content-Type':'application/binary'}

    r=requests.post(url,data=data,headers=headers)
    if r.status_code==200 and 'application/xml' in r.headers['content-type']:
        
        testo=r.content.decode('ISO-8859-2').encode('utf8')
        root=ET.fromstring(testo)
        articles=[]
        for title in root.iter('article-title'):
            articles.append([title.text])
    else:
        TRX.addUIMessage('Something went wrong, Cermine could not process your file')
        return TRX.returnOutput()

    for art in articles:
        title=art[0]
        new=TRX.addEntity('me.Article', title)
        try:
            author=art[1]
            year=art[2]
            new.addProperty('author','Author','loose', author)
            new.addProperty('year','Year','strict', str(year))
        except:
            pass

    logging(TRX.returnOutput(),m.Maltegoxml)
    return TRX.returnOutput()

