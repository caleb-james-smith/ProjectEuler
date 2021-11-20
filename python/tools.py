# tools.py

def pandigital(number):
    s = str(number)
    for i in range(1, len(s) + 1):
        if str(i) not in s:
            return False
    return True

