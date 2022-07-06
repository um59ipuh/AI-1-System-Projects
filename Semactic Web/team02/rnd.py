from sax_parser import *

if __name__ == "__main__":
    createRDFXML("rdfdata.rdf")
    r = open("zbMathOpen_OAIPMH_int.xml", 'r', encoding="utf-8")
    r.seek(22)
    MyHandler().parse(r)
