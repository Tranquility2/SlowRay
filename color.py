from vec3 import vec3

color = vec3  # Alias for clarity

def write_color(pixeel_color: color):
    r = pixeel_color.x
    g = pixeel_color.y
    b = pixeel_color.z

    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    return (rbyte, gbyte, bbyte)