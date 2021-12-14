def calc_minimum(numbers):
    a = numbers[0]
    for number in numbers:
        if number < a:
            a = number
    return a

def calc_maximum(numbers):
    a = numbers[0]
    for number in numbers:
        if number > a:
            a = number
    return a

def sort_ascend(numbers):
    answer_arr = []
    for number in numbers:
        while len(numbers) > 0:
            value = calc_minimum(numbers)
            answer_arr.append(value)
            numbers.remove(value)
    return answer_arr

def sort_descend(numbers):
    answer_arr = []
    for number in numbers:
        while len(numbers) > 0:
            value = calc_maximum(numbers)
            answer_arr.append(value)
            numbers.remove(value)
    return answer_arr
