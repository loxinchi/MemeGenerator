import pytest

from QuoteEngine import *


class Test_Ingestors():
    @pytest.mark.parametrize("ingestor_type, file_name", [(CSVIngestor, "DogQuotesCSV.csv"),
                                                          (DOCXIngestor, "DogQuotesDOCX.docx"),
                                                          (PDFIngestor, "DogQuotesPDF.pdf"),
                                                          (TXTIngestor, "DogQuotesTXT.txt")])
    def test_ingestors(self, ingestor_type, file_name, root):
        file_path = root / file_name
        result = ingestor_type.parse(file_path.as_posix())
        for quote in result:
            assert isinstance(quote, QuoteModel) is True
            assert len(quote.body) > 0
            assert len(quote.author) > 0
