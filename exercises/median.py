def median(pool):
    '''Statistical median to demonstrate doctest.
    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    7
    >>> median([1,2,3])
    2
    >>> median([1,2,3,4])
    2.5
    >>> l = [3,1,2]
    >>> median(l)
    2
    
    The original list has to be unaltered
    >>> l 
    [3, 1, 2]
    '''
    median = None

    return median
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()