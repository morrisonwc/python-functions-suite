# mysum.py

def mysum(number_list, starting_int=0):
    sum_output = starting_int

    for i in range(len(number_list)):
        try:
            sum_output += number_list[i]
        except TypeError:
            sum_output += 0

    return sum_output


print(mysum([5, True, 5.56, 'you FACE', 20, 'hello']))

