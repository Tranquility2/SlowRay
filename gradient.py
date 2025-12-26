# Generate a gradient image

from PIL import Image

def generate_gradient_image(width=256, height=256, filename="gradient.png"):
    image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r = float(x / (width - 1))
            g = float(y / (height - 1))
            b = 0.0
            ir = int(r * 255.999)
            ig = int(g * 255.999)
            ib = int(b * 255.999)
            image.putpixel((x, y), (ir, ig, ib))
    image.save(filename)
