import pathlib

import pytest

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()


@pytest.fixture()
def root():
    quotes_data = PROJECT_ROOT / "_data" / "DogQuotes"
    return quotes_data
