"""Choose the proper ingestor for a file."""
from typing import List

from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .IngestorInterface import IngestInterface
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor
from .exceptions import UnsupportedFileTypeError


class Ingestor(IngestInterface):
    """Ingestor object choose the proper ingestor for a file."""

    ingestors = [DOCXIngestor, CSVIngestor, PDFIngestor, TXTIngestor]
    support_type = ['docx', 'csv', 'pdf', 'txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify file extension matchs any of the ingestors.

        Choose the ingestor class to a file.

        :param path: File path that provides quote data.
        """
        extension = path.split(".")[-1]
        if extension not in cls.support_type:
            raise UnsupportedFileTypeError("Can't find any ingestor for this file.")

        for helper in cls.ingestors:
            if helper.can_ingest(path):
                return helper.parse(path)
