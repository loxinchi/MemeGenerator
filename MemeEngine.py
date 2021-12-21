"""A MemeEngine manipulates image file to a defined style."""
import os
from datetime import datetime

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
                text_w, text_h = draw.textsize(f"{text}\n-- {author}", font)
                draw.text(
                    ((width - text_w) - 1, (height - (text_h * 1.5)) - 1),
                    f"{text}\n-- {author}",
                    font=font,
                    fill="#52b69a",
                )
                draw.text(
                    ((width - text_w) + 1, (height - (text_h * 1.5)) - 1),
                    f"{text}\n-- {author}",
                    font=font,
                    fill="#52b69a",
                )
                draw.text(
                    ((width - text_w) - 1, (height - (text_h * 1.5)) + 1),
                    f"{text}\n-- {author}",
                    font=font,
                    fill="#52b69a",
                )
                draw.text(
                    ((width - text_w) + 1, (height - (text_h * 1.5)) + 1),
                    f"{text}\n-- {author}",
                    font=font,
                    fill="#52b69a",
                )
                draw.text(
                    (width - text_w, height - (text_h * 1.5)),
                    f"{text}\n-- {author}",
                    font=font,
                    fill="#ffba08",
                )

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
