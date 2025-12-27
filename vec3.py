class vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return self.length_squared() ** 0.5
    
    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2
    
    def cross(self, other):
        return vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def unit_vector(self):
        return self / self.length()

    def normalize(self):
        len = self.length()
        if len == 0:
            return vec3(0.0, 0.0, 0.0)
        return self / len

    def __repr__(self):
        return f"vec3({self.x}, {self.y}, {self.z})"
    
    def to_tuple(self):
        return (self.x, self.y, self.z)
