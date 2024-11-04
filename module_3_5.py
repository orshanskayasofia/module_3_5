def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(56743)
result3 = get_multiplied_digits(16002)
print(result1)
print(result2)
print(result3)

