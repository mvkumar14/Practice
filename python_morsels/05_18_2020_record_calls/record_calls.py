from functools import wraps
def record_calls(input_function):
    def wrapper(*args,**kwargs):
        wrapper.call_count += 1
        return input_function(*args,**kwargs)
    wrapper.call_count = 0
    return wrapper



@record_calls
def test():
    print("I'm inside the test function")

@record_calls
def test1():
    print("This is test 1")

print(test)
print(test.__dict__)
