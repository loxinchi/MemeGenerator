"""Validate MemeEngine class and generate_meme.

To run these tests from the project root, run:
    $ pytest -v test/test_meme.py
"""
import os

from meme import generate_meme
from MemeEngine import MemeEngine


def test_meme_engine(img_root):
    """Check MemeEngine generate file to the expected path."""
    img = img_root / "xander_1.jpg"
    output_dir = "./test_static"
    m = MemeEngine(output_dir)
    remake_img_path = m.make_meme(img, "quotes", "Author")
    assert remake_img_path == f"{output_dir}/resized.jpg"
    assert os.path.isfile(remake_img_path)


def test_generate_meme(img_root):
    """Check generate_meme generate file to the expected path."""
    img_path = img_root / "xander_1.jpg"
    output_path = generate_meme(img_path, "quotes", "Author")
    assert output_path == "./static/resized.jpg"
    assert os.path.isfile(output_path)
