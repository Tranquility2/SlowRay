# Generate a gradient image

from PIL import Image
from alive_progress import alive_bar
from color import color, write_color

def generate_gradient_image(width=256, height=256, filename="gradient.png"):
    image = Image.new("RGB", (width, height))
    with alive_bar(width * height, title="Generating Gradient Image") as bar:
        for x in range(width):
            for y in range(height):
                pixel_color = color(x / (width - 1), y / (height - 1), 0.0)
                image.putpixel((x, y), write_color(pixel_color))
                bar()
    image.save(filename)
