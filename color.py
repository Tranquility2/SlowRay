from vec3 import vec3

color = vec3  # Alias for clarity

def write_color(pixel_color: color):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    return (rbyte, gbyte, bbyte)