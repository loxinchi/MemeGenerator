"""CSVIngestor convert data form CSV file to a list of QuoteModel."""
from typing import List

import pandas

from .exceptions import WrongIngestorError
from .IngestorInterface import IngestInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestInterface):
    """CSVIngestor is a strategy object realise parse from the abstract IngestInterface."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify extension match CSV and parse data form CSV file a list of QuoteModel.

        :param path: File path that provides quote data.
        """
        if not cls.can_ingest(path):
            raise WrongIngestorError("Failed to ingest. This is not a CSV file.")

        quotes = []
        # initialise dataframe
        dataframe = pandas.read_csv(path, header=0)  # header in row 0

        for index, row in dataframe.iterrows():
            new_quote = QuoteModel(row["body"], row["author"])
            quotes.append(new_quote)

        return quotes
