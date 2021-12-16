"""Pytest fixtures."""
import pathlib

import pytest

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()


@pytest.fixture()
def quotes_root():
    """Input file path of all the quotes file."""
    quotes_data = PROJECT_ROOT / "_data" / "DogQuotes"
    return quotes_data


@pytest.fixture()
def img_root():
    """Input file path of all the image files."""
    quotes_data = PROJECT_ROOT / "_data" / "photos" / "dog"
    return quotes_data
