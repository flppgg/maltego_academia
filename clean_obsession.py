def clean_obsession(caccola):
    bastardi=['{','}','<','>','\\','/','&']
    for i in bastardi:
        caccola=caccola.replace(i,'')
    return caccola
