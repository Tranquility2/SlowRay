from gradient import generate_gradient_image

def main():
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    image_height = 1 if image_height < 1 else image_height
    generate_gradient_image(width=image_width, height=image_height, filename="gradient.png")

if __name__ == "__main__":
    main()
