"""Load resources and randomly choose one image and QuoteModel and render to html."""
import os
import random
from datetime import datetime

import requests
from flask import Flask, render_template, request

from Exceptions.exceptions import AuthorNoneTypeError, ImageBrokenError
from meme import generate_meme
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    # quote_files variable
    quotes = []
    for file in quote_files:
        quote = Ingestor.parse(file)
        quotes.append(quote)
    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    # use os.walk to discover ingestible files in a directory
    imgs = []

    for root, dirs, files in os.walk(images_path):
        for file_name in files:
            imgs.append(os.path.join(root, file_name))

    return quotes, imgs


all_quotes, all_images = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(all_images)
    doc_quotes = random.choice(all_quotes)
    quote = random.choice(doc_quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    # Save the image from the image_url form param to a temp local file.
    image_url = request.form["image_url"]
    # Adding current time
    now = datetime.now().strftime("%H_%M_%S")
    t_img = f"./temp_img{now}.jpg"
    try:
        img_content = requests.get(image_url, stream=True).content
        with open(t_img, "wb") as file:
            file.write(img_content)

        # generate a meme using temp file and the body and author form parameters.
        body = request.form["body"]
        author = request.form["author"]
        path = generate_meme(t_img, body, author)
    except requests.exceptions.RequestException as err:
        print(err)
        return render_template("meme_url_error.html")
    except AuthorNoneTypeError as err:
        print(err)
        return render_template("meme_author_error.html")
    except ImageBrokenError:
        return render_template("meme_image_error.html")

    # Remove the temporary saved image.
    os.remove(t_img)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(debug=True)
