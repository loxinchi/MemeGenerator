"""An abstract base class for each type of the ingestor."""
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestInterface(ABC):
    """IngestInterface is an abstract base class.

    Define the file extension verify method and
    parse method for each type of the ingestor.
    """

    # This list needs to be realised when each child class realise the parse
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Verify file extension as expected."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse data from file path.

        :param path: The file path.
        :return: A list of QuoteModel.
        """
        pass
