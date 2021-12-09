"""TXTIngestor convert data form TXT file to a list of QuoteModel."""
import re
from typing import List

from .exceptions import UnsupportedFileTypeError
from .IngestorInterface import IngestInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestInterface):
    """TXTIngestor is a strategy object realise parse from the abstract IngestInterface."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify extension match TXT and parse data form TXT file a list of QuoteModel.

        :param path: File path that provides quote data.
        """
        if not cls.can_ingest(path):
            raise UnsupportedFileTypeError("Failed to ingest. This is not a TXT file.")

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
