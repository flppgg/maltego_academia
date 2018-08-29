from Mylogging import logging
import json
from Maltego2 import *
from mendeley import Mendeley
from tokens import *

def trx_abstracts(m):
        
    TRX = MaltegoTransform()

    doi=m.getProperty("DOI")
    if not doi:
        TRX.addUIMessage('A DOI is needed to perform this search. Please run "Search on Crossref" and, if a DOI is found, try again here')
        return TRX.returnOutput()

    client_id=Tokens.MendeleyID
    client_secret = Tokens.MendeleySecret

    mendeley = Mendeley(client_id, client_secret=client_secret)
    auth = mendeley.start_client_credentials_flow()
    session = auth.authenticate()

    try:
        abstract = session.catalog.by_identifier(doi=doi).abstract
    except:
        TRX.addUIMessage( "Cannot find document on Mendeley")
    else:
        new = TRX.addEntity("me.Article", title)
        new.addProperty("abstract","Abstract", 'loose', abstract.encode('utf-8'))
        TRX.addUIMessage(abstract)

    logging(TRX.returnOutput(),m.Maltegoxml)
    return TRX.returnOutput()

