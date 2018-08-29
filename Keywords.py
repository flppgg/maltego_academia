from Mylogging import logging
from Maltego2 import *
from mendeley import Mendeley
from tokens import *

def trx_keywords(m):
        
    TRX = MaltegoTransform()
    try:
        keywords=[x for x in (m.getProperty("keywords").split('; '))]
        keywords=keywords[:12]
    except AttributeError:
        TRX.addUIMessage('Silly, there are no keywords for this article. But you could insert them yourself and then try again!')
        return TRX.returnOutput()
    limit=12
   # limit=m.getTransformSetting('HowMany')
    print limit
#    if not limit.isdigit():
#        TRX.addUIMessage('Silly! That has to be a number')
#        return TRX.returnOutput()
    if limit>40:
        TRX.addUIMessage("Sorry, that's too many! Currently the limit is 12 with the free Maltego, otherwise 50")
        return TRX.returnOutput()
    elif limit>12:
        TRX.addUIMessage("You set a value > than 12. If you are using the free Maltego, you are still going to get 12")
        return TRX.returnOutput()

    client_id=Tokens.MendeleyID
    client_secret= Tokens.MendeleySecret

    mendeley = Mendeley(client_id, client_secret=client_secret)
    auth = mendeley.start_client_credentials_flow()
    session = auth.authenticate()
    try:
        pages = [session.catalog.search(keyword).list() for keyword in keywords]
    except UnicodeEncodeError:
        TRX.addUIMessage("""Sorry, Mendeley doesn't accept keywords with non-latin characters. 
Please change them yourself and try again""")
        return TRX.returnOutput()

    n_results_per_key = limit / len(pages)
    if n_results_per_key == 0:
        n_results_per_key == 1

    keyplace=0
    for page in pages:
        if len(page.items) < n_results_per_key:
            limit=len(page.items)
        else:
            limit=n_results_per_key
        for n in range(limit):
            doc=page.items[n]
            new = TRX.addEntity("me.Article", doc.title.encode('utf-8'))
            new.setWeight(100-n)
#            new.setLinkColor('0x808000')
            new.setLinkLabel(keywords[keyplace].encode('utf-8'))
            try:
                new.addProperty("abstract","Abstract", True, doc.abstract.encode('utf-8'))
                new.addProperty("year","Year", False, str(doc.year))
                authori=[doc.authors[n].first_name.encode('utf-8')+' '+doc.authors[n].last_name.encode('utf-8') for n in range(0,len(doc.authors))]
                new.addProperty("author","Author", True, '; '.join(authori))
                doc_keywords=[doc.keywords[n].encode('utf-8') for n in range(len(doc.keywords))]
                new.addProperty("keywords","Keywords",True, '; '.join(doc_keywords))
                new.addProperty("DOI","DOI",'strict', doc.identifiers['doi'])
            except:
                TRX.addUIMessage('Article: '+doc.title.encode('utf-8')+'. Not all fields could be downloaded, probably keywords..')
        keyplace+=1

    logging(TRX.returnOutput(),m.Maltegoxml)

    return TRX.returnOutput()

