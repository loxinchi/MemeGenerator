"""Validate all the ingestors and possible error handling.

To run these tests from the project root, run:
    $ pytest -v test/test_ingestors.py
"""
import pytest

from QuoteEngine import *
from QuoteEngine.exceptions import UnsupportedFileTypeError, WrongIngestorError


@pytest.mark.parametrize(
    "ingestor_type, file_name",
    [
        (CSVIngestor, "DogQuotesCSV.csv"),
        (DOCXIngestor, "DogQuotesDOCX.docx"),
        (PDFIngestor, "DogQuotesPDF.pdf"),
        (TXTIngestor, "DogQuotesTXT.txt"),
    ],
)
def test_ingestors_by_type(ingestor_type: str, file_name: str, quotes_root) -> None:
    """Test ingestors by giving the matched type of file."""
    file_path = quotes_root / file_name
    result = ingestor_type.parse(file_path.as_posix())
    for quote in result:
        assert isinstance(quote, QuoteModel) is True
        assert len(quote.body) > 0
        assert len(quote.author) > 0


@pytest.mark.parametrize(
    "ingestor_type, file_name",
    [
        (CSVIngestor, "DogQuotesDOCX.docx"),
        (DOCXIngestor, "DogQuotesPDF.pdf"),
        (PDFIngestor, "DogQuotesTXT.txt"),
        (TXTIngestor, "DogQuotesCSV.csv"),
    ],
)
def test_negtive_ingestors_by_type(
    ingestor_type: str, file_name: str, quotes_root
) -> None:
    """Test ingestors by giving the unmatched type of file."""
    file_path = quotes_root / file_name
    with pytest.raises(WrongIngestorError) as exc_info:
        ingestor_type.parse(file_path.as_posix())
    ingestor_file_type = ingestor_type.__name__[:-8]
    assert (
        exc_info.value.message
        == f"Failed to ingest. This is not a {ingestor_file_type} file."
    )


@pytest.mark.parametrize(
    "file_name",
    ["DogQuotesCSV.csv", "DogQuotesDOCX.docx", "DogQuotesPDF.pdf", "DogQuotesTXT.txt"],
)
def test_ingestor(file_name: str, quotes_root) -> None:
    """Test the main ingestor by giving only he files."""
    file_path = quotes_root / file_name
    result = Ingestor.parse(file_path.as_posix())
    for quote in result:
        assert isinstance(quote, QuoteModel) is True
        assert len(quote.body) > 0
        assert len(quote.author) > 0


def test_no_ingestor(img_root) -> None:
    """Test the main ingestor by giving a unnsupported file type."""
    file_path = img_root / "xander_1.jpg"
    with pytest.raises(UnsupportedFileTypeError) as exc_info:
        Ingestor.parse(file_path.as_posix())
    assert exc_info.value.message == "Can't find any ingestor for this file."
