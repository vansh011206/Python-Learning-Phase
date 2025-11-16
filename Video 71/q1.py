# Class representing a 2D vector
class C2dVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_vector(self):
        print(f"2D Vector: ({self.x}, {self.y})")


# Class representing a 3D vector using C2dVector
class C3dVector(C2dVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # initialize x and y using parent class
        self.z = z

    def show_vector(self):
        print(f"3D Vector: ({self.x}, {self.y}, {self.z})")


# Example usage
v2d = C2dVector(3, 4)
v2d.show_vector()

v3d = C3dVector(3, 4, 5)
v3d.show_vector()
