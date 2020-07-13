# 3d vector class with multiple assignment , supports equality and inequality operators


class Vector():
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
    def __eq__(self,other):
        # if type(other) != '__main__.Vector':
        #     print("That isn't a valid comparison")
        #     return
        return (self.x, self.y, self.z)==(other.x, other.y, other.z)

v = Vector(1,2,3)
print(type(v))
print(v==Vector(1,2,3))
x, y, z = v
print(x, y, z)