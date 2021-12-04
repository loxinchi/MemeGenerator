from typing import List

import pandas

from IngestorInterface import IngestInterface
from QuoteModel import QuoteModel
from exceptions import UnsupportedFileTypeError


class CSVIngestor(IngestInterface):
    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise UnsupportedFileTypeError("Failed to ingest. This is not a CSV file.")

        quotes = []
        # initialise dataframe
        dataframe = pandas.read_csv(path, header=0)  # header in row 0

        for index, row in dataframe.iterrows():
            new_quote = QuoteModel(row["body"], row["author"])
            quotes.append(new_quote)

        return quotes


dataframe = pandas.read_csv('../_data/DogQuotes/DogQuotesCSV.csv', header=0)
for index, row in dataframe.iterrows():
    print(f'index: {index}\nrow:{row["body"]}')
