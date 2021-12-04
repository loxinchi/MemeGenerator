from abc import ABC, abstractmethod
from typing import List
from xmlrpc.client import boolean

from QuoteModel import QuoteModel


class IngestInterface(ABC):
    # This list needs to be realised when each child class realise the parse
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> boolean:
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
