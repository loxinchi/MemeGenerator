import re
from typing import List

from .IngestorInterface import IngestInterface
from .QuoteModel import QuoteModel
from .exceptions import UnsupportedFileTypeError


class TXTIngestor(IngestInterface):
    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise UnsupportedFileTypeError("Failed to ingest. This is not a CSV file.")

        quotes = []
        with open(path) as inputs:
            lines = inputs.readlines()
            if len(lines) > 0:
                for line in lines:
                    for match in re.finditer("([\w\. ]+) - ([\w ]+)+", line):
                        quote, author = match.groups()
                        new_quote = QuoteModel(quote, author)
                        quotes.append(new_quote)

        return quotes


# s = TXTIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt')
# print(s)
