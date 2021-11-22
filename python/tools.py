# tools.py

def pandigital(number):
    s = str(number)
    len_s = len(s)
    # require number to be 9 digits or less
    if len_s > 9:
        return False
    for i in range(1, len_s + 1):
        if str(i) not in s:
            return False
    return True

