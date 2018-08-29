from Mylogging import logging
from clean_obsession import *
from Maltego2 import *
import json
from mendeley import Mendeley
from tokens import *

def trx_searchauthor(m):
        
    TRX = MaltegoTransform()

    authore=m.getProperty("person.fullname")
    client_id=Tokens.MendeleyID
    client_secret= Tokens.MendeleySecret

    mendeley = Mendeley(client_id, client_secret=client_secret)
    auth = mendeley.start_client_credentials_flow()
    session = auth.authenticate()

    page = session.catalog.advanced_search(author=authore).list()


    if len(page.items) < 12:
        limit=len(page.items)
    else:
        limit=m.Slider
#    print m.Slider
#    print limit
        
    for n in range(limit):
        doc=page.items[n]
        titlee=clean_obsession(doc.title)
        new = TRX.addEntity("me.Article", titlee)
        new.setWeight(100-n)
        try:
            new.addProperty("abstract","Abstract", 'strict', clean_obsession(doc.abstract).encode('utf-8'))
            new.addProperty("year","Year", 'strict', str(doc.year))
            new.addProperty("DOI","DOI",'strict', doc.identifiers['doi'])
            authori=[doc.authors[n].first_name.encode('utf-8')+' '+doc.authors[n].last_name.encode('utf-8') for n in range(len(doc.authors))]
            new.addProperty("author","Author", 'strict', clean_obsession('; '.join(authori)))
            if doc.keywords:
                doc_keywords=[doc.keywords[n].encode('utf-8') for n in range(len(doc.keywords))]
                new.addProperty("keywords","Keywords",'strict', clean_obsession('; '.join(doc_keywords)))
        except:
#              pass
  #           print 'o dear'
             TRX.addUIMessage('Article: '+titlee+'. Not all fields could be downloaded')
 #       print titlee
#    print TRX.returnOutput()
#    print 'santa madonna'
    logging(TRX.returnOutput(),m.Maltegoxml)
    return TRX.returnOutput()


