import pathlib

import pytest

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()


@pytest.fixture()
def quotes_root():
    quotes_data = PROJECT_ROOT / "_data" / "DogQuotes"
    return quotes_data


@pytest.fixture()
def img_root():
    quotes_data = PROJECT_ROOT / "_data" / "photos" / "dog"
    return quotes_data
