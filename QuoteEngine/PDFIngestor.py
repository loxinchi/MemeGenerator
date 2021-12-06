import os
import random
import re
import subprocess
from typing import List

from .IngestorInterface import IngestInterface
from .QuoteModel import QuoteModel
from .exceptions import UnsupportedFileTypeError


class PDFIngestor(IngestInterface):
    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise UnsupportedFileTypeError("Failed to ingest. This is not a CSV file.")

        quotes = []
        tmp = f"{random.randint(0, 1000000)}.txt"
        subprocess.run(['pdftotext', path, tmp])
        with open(tmp) as fp:
            for line in fp.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    for match in re.finditer('("[\w\\\' ]+") - ([\w ]+)+', line):
                        quote, author = match.groups()
                        new_quote = QuoteModel(quote, author.strip())
                        quotes.append(new_quote)

        os.remove(tmp)
        return quotes


# s = PDFIngestor.parse("../_data/DogQuotes/DogQuotesPDF.pdf")
# print(s)
# if __name__ == '__main__':
#     quotes = []
#     tmp = f'{random.randint(0, 1000000)}.txt'
#     # print(tmp)
#     p = subprocess.run(['pdftotext', '../_data/DogQuotes/DogQuotesPDF.pdf', tmp])
    # with open(tmp) as fp:
    #     for line in fp.readlines():
    #         print(line)

# quotes = '"Treat yo self" - Fluffles "Life is like a box of treats" - Forrest Pup "It\'s the size of the fight in the dog" - Bark Twain'
# filter_line = re.findall("\"[\w\\' ]+\" - [\w ]+", quotes)
# print(f"line: {filter_line}")
# for match in re.finditer("(\"[\w\\' ]+\") - ([\w ]+)+", quotes):
#     quote, author = match.groups()
#     print(f"{quote}, {author}")

# if len(line) > 0:
#     parsed = line.split(' ')
#     # print(f"parsed: {parsed}")
#     quote = [quote_items.split(',') for quote_items in parsed]
#     print(quote)
