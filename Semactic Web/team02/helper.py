# this file contains all helper functions
import urllib.parse as encode


def createRDFXML(file: str):
    with open(file, 'a') as f:
        f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        f.write("\n")
        f.write("<rdf:RDF\n")
        f.write("\txmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n")
        f.write("\txmlns:info=\"https://zbmath.org/infos#\">\n")
        f.write("\n")


def append_record_rdf(file: str, desc, infos):
    with open(file, 'a') as f:
        f.write(desc)
        for info in infos:
            f.write(f"\t{info}")
        f.write("\t\t</rdf:Description>\n")
        f.write("\n")


def close_rdf_xml(file: str):
    with open(file, 'a') as f:
        f.write("</rdf:RDF>")


def get_new_rdf(doc_id: str):
    return f"\t\t<rdf:Description rdf:about=\"https://zbmath.org/?q=an%3A{encode_value(doc_id)}\">\n"


def get_classification(val: str):
    return f"\t\t<info:classification rdf:resource=\"https://zbmath.org/classification/?q=cc%3A{encode_value(val)}\"/>\n"


def get_author(val: str):
    return f"\t\t<info:author rdf:resource=\"https://zbmath.org/authors/?q=ai%3A{encode_value(val)}\"/>\n"


def get_keyword(val: str):
    return f"\t\t<info:keyword rdf:resource=\"https://zbmath.org/?q=ut%3A{encode_value(val)}\"/>\n"


def get_publication_date(val: str):
    return f"\t\t<info:year>{val}</info:year>\n"


def encode_value(val: str) -> str:
    return encode.quote_plus(val)