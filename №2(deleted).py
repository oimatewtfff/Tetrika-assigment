import math


def task(x1, y1, x2, y2, x3, y3, x4, y4):

    if x1 < x3 < x2 and y1 < y3 < y2:
        return True, f'S = {math.sqrt((x2-x3)**2) * math.sqrt((y3-y2)**2)}'
    elif x1 < x4 < x2 and y1 < y4 < y2:
        return True, f'S = {math.sqrt((x4-x2)**2) * math.sqrt((y4-y2)**2)}'
    elif x1 < x3 < x2 and y1 < y4 < y2:
        return True, f'S = {math.sqrt((x3-x2)**2) * math.sqrt((y4-y2)**2)}'
    elif x1 < x4 < x2 and y1 < y3 < y2:
        return True, f'S = {math.sqrt((x4-x2)**2) * math.sqrt((y3-y2)**2)}'
    return False


print(task(1, 1, 2, 2, 3, 3, 4, 4))  # OUT: False
print(task(0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0))  # OUT: False
print(task(0.5, 1.0, 2.5, 2.0, 1.5, 0.5, 2.5, 1.5))  # OUT: True
print(task(0.5, 1.0, 2.5, 2.0, 0.5, 1.5, 1.5, 2.5))  # OUT: True
print(task(0.5, 1.0, 2.5, 2.0, 0.5, 0.5, 1.5, 1.5))  # OUT: True
print(task(0.5, 1.0, 2.5, 2.0, 1.5, 1.5, 2.5, 2.5))  # OUT: True
print(task(0, 1.0, 2.5, 2.0, 1.5, 1.5, 2, 4))  # OUT: True
print(task(0, 0, 2.5, 2.0, 1.5, 1.5, 2, 4))  # OUT: True
print(task(1.5, 1.5, 2.5, 2.5, 2, 2, 4, 4))  # OUT: True
