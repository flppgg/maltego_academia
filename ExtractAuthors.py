from Maltego2 import *
from Mylogging import logging

def trx_extractauthors(m):
    
#    data=open('/home/ubuntu/1.pdf','rb').read()
    TRX = MaltegoTransform()
    try:
        authorss = m.getProperty("author")
    except:
        TRX.addUIMessage('Sorry, it appears the article has no Author')
        return TRX.returnOutput()
    authors = authorss.split("; ")
    for i in authors:
        if i is not '':
            new=TRX.addEntity("maltego.Person",i)
#            new.addProperty('binary','Binary','strict',data)
            new.addDisplayInformation('<a href="C:\\Users\\carla\\Documents\\aa.pdf"> rrr </a>','rrr')
#    logging(TRX.returnOutput(),m.testo)
    logging(TRX.returnOutput(),m.Maltegoxml)
    return TRX.returnOutput()

