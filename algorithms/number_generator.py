def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'

    no_pattern = ''
    for x in range(1, n+1):

        no_pattern +=(str(x))
        if x < n:
            no_pattern += (str(' '))
        
    return no_pattern



print(number_pattern(78))
