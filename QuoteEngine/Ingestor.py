from typing import List

from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .IngestorInterface import IngestInterface
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor


class Ingestor(IngestInterface):
    ingestors = [DOCXIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for helper in cls.ingestors:
            if helper.can_ingest(path):
                return helper.parse(path)
