def adder(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result







#"""
#>>> 2+2
#5
#"""
#if __name__ == "__main__":
#    import doctest
#doctest.testmod()