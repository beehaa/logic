def negabase(number, base):
    """ Calculates the decimal value of a number
        in a given negative base """
    hbase = 1
    sign = 1
    result = 0
    while number>0:
        digit = number % 10
        result += sign*hbase*digit
        number = int(number / 10)
        sign = -1*sign
        hbase *= base
    return result
