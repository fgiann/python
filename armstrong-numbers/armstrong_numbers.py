def is_armstrong_number(number):
    digits = len(str(number))
    tmp = number
    digits_sum = 0
    
    while tmp > 0:
        digits_sum += (tmp % 10) ** digits
        tmp = tmp // 10
    
    return digits_sum == number
    