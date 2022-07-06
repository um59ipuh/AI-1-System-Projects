import xml.sax as parser
from helper import *
import pathlib

class RDFData:
    def __init__(self, doc_id, class_, authors, keywards):
        self.document_id = doc_id
        self.classifications = class_
        self.authors = authors
        self.keywards = keywards


class MyHandler(parser.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._result = []
        self.counter = 0

        self.current_tag = ""
        self.is_new_started = True
        self.infos = []
        self.desc = ""

    def _getCharacterData(self):
        data = ''.join(self._charBuffer)
        self._charBuffer = []
        return data

    def parse(self, f):
        parser.parse(f, self)

    def characters(self, data):

        if self.current_tag == "record" and self.is_new_started:
            # track for single rdf description
            # add new record rdf
            self.is_new_started = False
            pass

        if self.current_tag == 'zbmath:document_id':
            print(f"Document id: {str(data).strip()}")
            self.desc = get_new_rdf(str(data).strip())

        if self.current_tag == 'zbmath:classification':
            print(f"Classification id: {str(data).strip()}")
            self.infos.append(get_classification(str(data).strip()))

        if self.current_tag == 'zbmath:author_id':
            print(f"Author id: {str(data).strip()}")
            self.infos.append(get_author(str(data).strip()))

        if self.current_tag == 'zbmath:keyword':
            print(f"Keyword id: {str(data).strip()}")
            self.infos.append(get_keyword(str(data).strip()))

        if self.current_tag == 'zbmath:publication_year':
            print(f"Year id: {str(data).strip()}")
            self.infos.append(get_publication_date(str(data).strip()))



    def startElement(self, name, attrs):
        if name == 'record':
            self.current_tag = "record"

        if name == 'zbmath:document_id':
            self.current_tag = "zbmath:document_id"

        if name == 'zbmath:classification':
            self.current_tag = "zbmath:classification"

        if name == 'zbmath:author_id':
            self.current_tag = "zbmath:author_id"

        if name == 'zbmath:keyword':
            self.current_tag = "zbmath:keyword"

        if name == 'zbmath:publication_year':
            self.current_tag = "zbmath:publication_year"

    def endElement(self, name):

        if name == "record" and not self.is_new_started:
            append_record_rdf("rdfdata.rdf", self.desc, self.infos)
            # reset data and flag
            self.desc = ""
            self.infos = []
            self.is_new_started = True

            self.current_tag = ""

        if name == 'zbmath:document_id':
            self.current_tag = ""

        if name == 'zbmath:classification':
            self.current_tag = ""

        if name == 'zbmath:author_id':
            self.current_tag = ""

        if name == 'zbmath:keyword':
            self.current_tag = ""

        if name == "zbmath:publication_year":
            self.current_tag = ""

    def endDocument(self):
        print(f"Document is finished to read")
        # close file
        close_rdf_xml("rdfdata.rdf")


def buildRdfDataFile(filename):
    abs_file_path = pathlib.Path(filename).absolute()
    createRDFXML("rdfdata.rdf")
    r = open(abs_file_path, "r")
    r.seek(22)
    MyHandler().parse(r)

if __name__ == "__main__":
    createRDFXML("rdfdata.rdf")
    r = open("workingdata.xml", "r")
    r.seek(22)
    MyHandler().parse(r)