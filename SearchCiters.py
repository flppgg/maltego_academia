from Mylogging import logging
import scholarly
from Maltego2 import *
from unidecode import unidecode
from clean_obsession import *

bastardi=['{','}','<','>']

def trx_searchciters(m):
    
    TRX = MaltegoTransform()
    title=m.getProperty("title.article")
    title=unidecode(title)
#    print title
    DOI=m.getProperty("DOI")
    if DOI:
        query=DOI
    else:
        query=title
    search_query = scholarly.search_pubs_query(query)

    try:
         result=next(search_query)
    except StopIteration:
        TRX.addUIMessage("""The DOI could not be found on Google Scholar, 
which very likely means Google Scholar has never heard of this article before""")
        return TRX.returnOutput()

    titlemaybe=result.bib['title']

    TRX.addUIMessage("""Title found: %s. 
If this is not what you were looking for, add the article's DOI and search again""" % make_unicode(clean_obsession(titlemaybe)), UIM_INFORM)

    limit=m.slider
    count=0

    for citation in result.get_citedby():

        if count==limit:
            break

        for i in bastardi:
            title=citation.bib['title'].replace(i, '')
        new = TRX.addEntity("me.Article", title.encode('utf-8'))

#        new.setLinkLabel('Cited by')
#        new.setLinkColor('blue')
#        new.setLinkThickness(2)

        authors='; '.join([authore for authore in citation.bib['author'].split(' and ')])
        for i in bastardi:
            authors=authors.replace(i, '')
        new.addProperty("author","Author", "loose", authors.encode('utf-8')) 

        count+=1

    logging(TRX.returnOutput(),m.Maltegoxml)

    return TRX.returnOutput()

