# Generate a gradient image

from PIL import Image
from alive_progress import alive_bar

def generate_gradient_image(width=256, height=256, filename="gradient.png"):
    image = Image.new("RGB", (width, height))
    with alive_bar(width * height, title="Generating Gradient Image") as bar:
        for x in range(width):
            for y in range(height):
                r = float(x / (width - 1))
                g = float(y / (height - 1))
                b = 0.0
                ir = int(r * 255.999)
                ig = int(g * 255.999)
                ib = int(b * 255.999)
                image.putpixel((x, y), (ir, ig, ib))
                bar()
    image.save(filename)
