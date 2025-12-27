from PIL import Image
from alive_progress import alive_bar
from color import color, write_color
from vec3 import vec3, point3
from ray import ray

def ray_color(r: ray) -> color:
    unit_direction = r.direction.unit_vector()
    a = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - a) * color(1.0, 1.0, 1.0) + a * color(0.5, 0.7, 1.0)

# Generate a gradient image and save it to a file
def generate_gradient_image(image: Image, filename: str):
    # Camera setup
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * (image.width / image.height)
    camera_center = point3(0, 0, 0)

    # calculate horizontal and vertical vectors
    viewport_u : vec3 = vec3(viewport_width, 0, 0)
    viewport_v : vec3 = vec3(0, -viewport_height, 0)

    # calculate horizontal and vertical vectors from pixel to pixel
    pixel_delta_u: vec3 = viewport_u / image.width
    pixel_delta_v: vec3 = viewport_v / image.height

    # calculate upper left corner of the viewport
    viewport_upper_left = (camera_center - vec3(0,0,focal_length) - viewport_u / 2 - viewport_v / 2)
    pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)
    with alive_bar(image.width * image.height, title="Generating Gradient Image") as bar:
        for x in range(image.width):
            for y in range(image.height):
                pixel_center = pixel00_loc + (x * pixel_delta_u) + (y * pixel_delta_v)
                ray_direction = pixel_center - camera_center
                r: ray = ray(camera_center, ray_direction)
                
                pixel_color: color = ray_color(r)
                write_color(image, x, y, pixel_color)
                
                bar()

    image.save(filename)

