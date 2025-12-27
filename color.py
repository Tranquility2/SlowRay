from PIL import Image
from vec3 import vec3

color = vec3  # Alias for clarity

# Write the color to the image at the specified pixel location
def write_color(image: Image.Image, x: int, y: int, pixel_color: color):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    image.putpixel((x, y), (rbyte, gbyte, bbyte))