def equilateral(sides):
    if not identity_condition(*sides):
        return False

    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    if not identity_condition(*sides):
        return False

    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    if not identity_condition(*sides):
        return False

    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]


def identity_condition(side1, side2, side3):
    is_valid_triangle = False

    if side1 > 0 and side2 > 0 and side3 > 0:
        condition1 = side1 + side2 >=side3
        condition2 = side1 + side3 >=side2
        condition3 = side2 + side3 >=side1

        is_valid_triangle = condition1 and condition2 and condition3


    return is_valid_triangle