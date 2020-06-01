Hey!

This week I'd like you to create a context manager. Context managers use a with block to bookend a block of code with automatic setup and teardown steps.

Your context manager, suppress, should suppress exceptions of a given type:

>>> with suppress(NameError):
...     print("Hi!")
...     print("It's nice to meet you,", name)
...     print("Goodbye!")
...
Hi!
>>> with suppress(TypeError):
...     print("Hi!")
...     print("It's nice to meet you,", name)
...     print("Goodbye!")
...
Hi!
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
NameError: name 'name' is not defined
>>> x = 0
>>> with suppress(ValueError):
...     x = int('hello')
...
>>> x
0

What I mean by "suppress" is that if the given exception type is raised, that exception should be caught and muted in a sense. As is common in other exception-handling in Python, child classes of the given exception type should be caught and muted as well.

To solve this exercise, you'll want to lookup how to create a context manager in Python.

Bonus 1

For the first bonus, I'd like you to make your suppress context manager accept any number of exceptions to suppress ✔️:

>>> with suppress(ValueError, TypeError):
...     x = int('hello')
...
>>> with suppress(ValueError, TypeError):
...     x = int(None)
...

Bonus 2

For the second bonus, I'd like you to allow your context manager to store the exception and traceback information on an object that can be accessed using the with X as Y syntax ✔️:

>>> with suppress(ValueError, TypeError) as context:
...     x = int('hello')
...
>>> context.exception
ValueError("invalid literal for int() with base 10: 'hello'",)
>>> context.traceback
<traceback object at 0x7fe829bc3bc8>

The exception and traceback attributes should be None when no exception was suppressed.

Bonus 3

If you manage to solve the main problem and both of the first two bonuses with time remaining, I have a third bonus for you.

For the third bonus I'd like you to allow your context manager to be used as a decorator as well ✔️:

>>> @suppress(TypeError)
... def len_or_none(thing):
...     return len(thing)
...

This decorator should essentially wrap your function in a call to the suppress context manager:

>>> len_or_none('hello')
5
>>> len_or_none(64)
>>> len_or_none([2, 4, 8])
3
>>> len_or_none()
>>> len_or_none([])
0

Hints

Hints for when you get stuck (hover over links to see what they're about):

    What is a context manager?
    How to write a context manager
    Handling exceptions in a context manager
    Checking if an item is an exception
    A helper for writing context managers
    Accepting any number of exception types
    Returning an object with the with ... as syntax
    Helper tools for writing decorators
    Using a context manager as a decorator
