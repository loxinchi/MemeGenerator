import os

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
            # Adjust text position align with image height and width
            w, h = img.size
            text_w, text_h = draw.textsize(f'{text}\n-- {author}', font)
            draw.text((w - text_w, h - (text_h*1.5)), f'{text}\n-- {author}', font=font, fill='#3867d6')

            # create output_dir if not exists
            if not os.path.exists(self.output_dir):
                # mode
                mode = 0o777
                os.mkdir(self.output_dir, mode)
            try:
                # Saving the manipulated image.
                img.save(self.output_dir + '/resized.jpg')
            except OSError:
                print(f'Only support jpg file.')

        return f'{self.output_dir}/resized.jpg'


# if __name__ == '__main__':
#     s = MemeEngine('/Users/xinchilo/Desktop/')
#     print(s.make_meme('/Users/xinchilo/Desktop/maxresdefault.jpeg', 'puppy', 'yuu', 500))
