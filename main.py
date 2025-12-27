from PIL import Image
from gradient import generate_gradient_image

def main():
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    image_height = 1 if image_height < 1 else image_height

    image = Image.new("RGB", (image_width, image_height))
    generate_gradient_image(image, "gradient.png")

if __name__ == "__main__":
    main()
