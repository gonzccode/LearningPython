
def suma(a=0, b=0):
    try:
        if type(a) == int and type(b) == int:
            return a + b
        else:
            return "Error"
    except TypeError:
        return 0
