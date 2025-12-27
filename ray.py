from vec3 import vec3, point3

class ray:
    def __init__(self, origin: point3, direction: vec3):
        self.origin = origin
        self.direction = direction

    def at(self, t: float) -> point3:
        return self.origin + t * self.direction
    
    def __repr__(self) -> str:
        return f"ray(origin={self.origin}, direction={self.direction})"
    