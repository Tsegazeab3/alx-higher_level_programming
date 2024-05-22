# Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class"""
    return type(obj) == a_class
if __name__ == ("__main__"):
    import doctest
    doctest.testfile("tests/2-is_same_class.txt")