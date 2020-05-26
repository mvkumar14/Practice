def decorator(my_class):
    obj = my_class()
    class Test():
        def __init__(self):
            self.a = obj.a
            self.b = obj.b
    print('successfully did some stuff?')
    return Test

@decorator
class Whoahdude():
    def __init__(self):
        self.a = 1
        self.b = 2

def object_pass(my_obj):
    return 1

@object_pass
a = Whoahdude()

print(a)


# print(type(Whoahdude()))

# a = Whoahdude()
# print(type(a))
# print(a.a)
