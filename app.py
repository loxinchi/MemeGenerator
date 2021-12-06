import os
import random
import requests
from flask import Flask, abort, render_template, request

# [DONE]@TODO Import your Ingestor and MemeEngine classes
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
from meme import generate_meme

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    # [DONE]TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quote = Ingestor.parse(file)
        quotes.append(quote)
    # quotes = None

    images_path = "./_data/photos/dog/"

    # [DONE]TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    # use os.walk to automatically discover ingestible files in a directory
    imgs = []

    for root, dirs, files in os.walk(images_path):
        for file_name in files:
            imgs.append(os.path.join(root, file_name))

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    doc_quotes = random.choice(quotes)
    quote = random.choice(doc_quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""
    # It uses the requests package to fetch an image from a user submitted URL.
    # @TODO:
    # 1. Use requests to save the image from the image_url form param to a temp local file.
    image_url = request.form['image_url']
    t_img = "./temp_img.jpg"
    img_content = requests.get(image_url, stream=True).content
    with open(t_img, 'wb') as f:
        f.write(img_content)
    # 2. Use the meme object to generate a meme using this temp file and the body and author form paramaters.
    body = request.form['body']
    author = request.form['author']
    path = generate_meme(t_img, body, author)

    # 3. Remove the temporary saved image.
    os.remove(t_img)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()

# TODO: If the program encounters a common error case (e.g. attempting to load an incompatible filetype), it throws an exception.
#
# All exceptions include a human-readable message.
#
# (Optional) Make your exception handling even more awesome:
#
# Define custom exception classes for different types of exceptions—for things like *Invalid File, Invalid Text Input (e.g. too long)
# Use os.walk to automatically discover ingestible files in a directory
