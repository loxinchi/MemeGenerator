"""A MemeEngine manipulates image file to a defined style."""
import os
import textwrap
from datetime import datetime
from string import ascii_letters

from PIL import Image, ImageDraw, ImageFont

from Exceptions.exceptions import ImageBrokenError


class MemeEngine:
    """A MemeEngine Object encapsulate resize, add text, reformat and generate a new image."""

    def __init__(self, output_dir: str) -> None:
        """Create a new `MemeEngine`.

        :param output_dir: An image output path.
        """
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """Resize, add quote and author, reformat image inorder to properly render to web UI.

        :param img_path: An image input path.
        :param text: The quote body.
        :param author: The author name of the quote.
        :param width: Image width.
        """
        # Load image
        try:
            with Image.open(img_path) as input_image:
                # Resize image so the width is at most 500px and the height is scaled proportionally.
                width_percent = width / float(input_image.size[0])
                height_size = int((float(input_image.size[1]) * float(width_percent)))
                img = input_image.resize((width, height_size), Image.ANTIALIAS)

                # Adding a quote body and a quote author to the image.
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(
                    "./_data/font/MesloLGS NF Regular.ttf", size=20
                )

                # Adjust text position align with image height and width
                width, height = img.size
                text_origin = f"{text}\n--{author}"
                # Calculate the average length of a single character of our font.
                char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(
                    ascii_letters
                )
                # Translate this average length into a character count
                # to fill 95% of our image's total width
                max_char_count = int((width * 0.618) / char_width)
                # Create a wrapped text object using scaled character count
                scaled_text = textwrap.fill(text=text_origin, width=max_char_count)

                # Add two colors to the text
                draw.text(xy=(10, 10), text=scaled_text, font=font, fill="#ffba08")
                draw.text(xy=(11, 11), text=scaled_text, font=font, fill="#FF5733")

                if not os.path.exists(self.output_dir):
                    mode = 0o777
                    os.mkdir(self.output_dir, mode)

                now = datetime.now().strftime("%H_%M_%S")
                output_path = self.output_dir + f"/resized{now}.jpg"
                img.convert("RGB")
                img.save(output_path)
        except (OSError, ValueError):
            raise ImageBrokenError

        return output_path

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"MemeEngine(output_dir = {self.output_dir})"
