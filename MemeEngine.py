"""A MemeEngine manupulates image file to a defined style."""
import os

from PIL import Image, ImageDraw, ImageFont


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
        with Image.open(img_path) as im:
            # Resizing the image so the width is at most 500px and the height is scaled proportionally.
            width_percent = width / float(im.size[0])
            height_size = int((float(im.size[1]) * float(width_percent)))
            img = im.resize((width, height_size), Image.ANTIALIAS)

            # Adding a quote body and a quote author to the image.
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(
                "~/Library/Fonts/MesloLGS NF Regular.ttf", size=20
            )

            # Adjust text position align with image height and width
            w, h = img.size
            text_w, text_h = draw.textsize(f"{text}\n-- {author}", font)
            draw.text(((w - text_w) - 1, (h - (text_h * 1.5)) - 1), f"{text}\n-- {author}", font=font, fill="#52b69a")
            draw.text(((w - text_w) + 1, (h - (text_h * 1.5)) - 1), f"{text}\n-- {author}", font=font, fill="#52b69a")
            draw.text(((w - text_w) - 1, (h - (text_h * 1.5)) + 1), f"{text}\n-- {author}", font=font, fill="#52b69a")
            draw.text(((w - text_w) + 1, (h - (text_h * 1.5)) + 1), f"{text}\n-- {author}", font=font, fill="#52b69a")
            draw.text(
                (w - text_w, h - (text_h * 1.5)),
                f"{text}\n-- {author}",
                font=font,
                fill="#ffba08",
            )

            # create output_dir if not exists
            if not os.path.exists(self.output_dir):
                mode = 0o777
                os.mkdir(self.output_dir, mode)
            try:
                img.convert("RGB")
                img.save(self.output_dir + "/resized.jpg")
            except OSError:
                print(f"Only support jpg file.")

        return f"{self.output_dir}/resized.jpg"


# if __name__ == '__main__':
#     s = MemeEngine('/Users/xinchilo/Desktop/')
#     print(s.make_meme('/Users/xinchilo/Desktop/maxresdefault.jpeg', 'puppy', 'yuu', 500))
