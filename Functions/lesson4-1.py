"""
Functions are blocks of code that we can call to excute
"""
def my_function():
    """
    Parameters:
        Nothing
    ----------------------------------------------------------
    Returns:
        Nothing
    """
    print("This function only prints!!!\n")

def add_num(a,b):
    """
    Parameters:
        a - a number (int > 0)
        b - a number (int > 0)
    ----------------------------------------------------------
    Returns:
        c - sum of a plus b (int)

    """
    c = a + b
    return c

def calc_diamater(radius):
    """
    Parameters:
        radius - radius of a circle (float > 0)
    -----------------------
    Returns:
        diam - diameter of the circle (float)
    """
    return radius*2

my_function()
a = 5
b = 2
c = add_num(a,b)
print(c)

