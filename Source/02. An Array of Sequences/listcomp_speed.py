from timeit import repeat

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

TIMES = 1000000


def clock(label, stmt):
    result = repeat(stmt=stmt, setup=SETUP, number=TIMES)
    print(f'{label:19}', ':', *(f'{x:.3f}' for x in result))


clock('listcomp', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + function', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + function', 'list(filter(non_ascii, map(ord, symbols)))')
