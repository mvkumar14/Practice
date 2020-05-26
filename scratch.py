def add_1(a):
    self.a += 1
    return a + 1

class_dict = {'a':0,'increment_a':add_1}

dyn_class = type('Test',(object,),class_dict)

print(dyn_class.__name__)
print(dir(dyn_class))

print(dyn_class.increment_a(2))