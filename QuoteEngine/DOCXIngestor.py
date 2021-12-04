from typing import List

import docx
from IngestorInterface import IngestInterface
from QuoteModel import QuoteModel
from exceptions import UnsupportedFileTypeError


class DOCXIngestor(IngestInterface):
    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise UnsupportedFileTypeError("Failed to ingest. This is not a DOCX file.")

        quotes = []
        doc = docx.Document(path)

        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                parsed = [parse.strip() for parse in paragraph.text.split("-")]
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        return quotes


doc = docx.Document('../_data/DogQuotes/DogQuotesDOCX.docx')

for paragraph in doc.paragraphs:
    # print(paragraph.text.replace('"', ''))
    if paragraph.text != "":
        parsed = [parse.strip() for parse in paragraph.text.split('-')]
        print(f'0:{parsed[0]}, '
              f'1:{parsed[1]}')
