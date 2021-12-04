from PIL import Image, ImageDraw, ImageFont


class MemeEngine:

    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        # Load image
        with Image.open(img_path) as im:
            # Resizing the image so the width is at most 500px and the height is scaled proportionally.
            width_percent = (width / float(im.size[0]))
            height_size = int((float(im.size[1]) * float(width_percent)))
            img = im.resize((width, height_size), Image.ANTIALIAS)

            # Adding a quote body and a quote author to the image.
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('~/Library/Fonts/MesloLGS NF Regular.ttf', size=20)
            draw.text((10, 30), f'{text} - {author}', font=font, fill='white')
            # Saving the manipulated image.
            img.save(self.output_dir + 'resized.jpg')

        return f'{self.output_dir}resized.jpg'


# if __name__ == '__main__':
#     s = MemeEngine('/Users/xinchilo/Desktop/')
#     print(s.make_meme('/Users/xinchilo/Desktop/maxresdefault.jpeg', 'puppy', 'yuu', 500))
