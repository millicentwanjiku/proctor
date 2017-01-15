"""Manipulating data"""
def manipulate_data(arg):
    """Returns summation of positive and negative integers"""
    if isinstance(arg, list):
        return [sum(1 for x in arg if isinstance(x, int) and x >= 0),
                 sum(x for x in arg if isinstance(x, int) and x < 0)]
    else:
        return 'Only lists allowed'

