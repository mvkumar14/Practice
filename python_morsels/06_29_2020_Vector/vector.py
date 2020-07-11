k# 3d vector class with multiple assignment , supports equality and inequality operators


class Vector():
    __slots__ = ('x','y','z')
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    