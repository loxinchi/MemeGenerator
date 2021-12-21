"""PDFIngestor convert data form PDF file to a list of QuoteModel."""
import os
import random
import re
import subprocess
from typing import List

from Exceptions.exceptions import WrongIngestorError
from .IngestorInterface import IngestInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestInterface):
    """PDFIngestor is a strategy object realise parse from the abstract IngestInterface."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify extension match PDF and parse data form PDF file a list of QuoteModel.

        :param path: File path that provides quote data.
        """
        if not cls.can_ingest(path):
            raise WrongIngestorError("Failed to ingest. This is not a PDF file.")

        quotes = []
        tmp = f"{random.randint(0, 1000000)}.txt"
        subprocess.run(["pdftotext", path, tmp])
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
