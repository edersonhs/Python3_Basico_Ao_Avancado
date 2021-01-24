x = "hello"

# if condition returns True, then nothing happens:
assert x == "hello"

# if condition returns False, AssertionError is raised:
# assert x == "goodbye"

"""
You can write a message to be written if the code returns False, check the
example below.
"""
# if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"
