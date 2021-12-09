"""DOCXIngestor convert data form DOCX file to a list of QuoteModel."""
from typing import List

import docx

from .exceptions import UnsupportedFileTypeError
from .IngestorInterface import IngestInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestInterface):
    """DOCXIngestor is a strategy object realise parse from the abstract IngestInterface."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify extension match DOCX and parse data form DOCX file a list of QuoteModel.

        :param path: File path that provides quote data.
        """
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
