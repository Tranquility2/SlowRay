from PIL import Image, ImageDraw

def main():
    image_hight = 256
    image_weidth = 256

    image = Image.new("RGB", (image_weidth, image_hight))
    for x in range(image_weidth):
        for y in range(image_hight):
            r = float(x / ((image_weidth - 1)))
            g = float(y / ((image_hight - 1)))
            b = 0.0
            ir = int(r * 255.999)
            ig = int(g * 255.999)
            ib = int(b * 255.999)
            image.putpixel((x, y), (ir, ig, ib))
    image.save("gradient.png")

if __name__ == "__main__":
    main()
