# def square(num):
#     result = num * num
#     return result
#
#
# a = square(4)
# print a
# square(10)
#

def validate(prompt, low, high, ok, not_ok):
    input_from_user = int(input(prompt))
    if low < input_from_user < high:
        print(ok)
    else:
        print(not_ok)


validate("enter your age:", 0, 120, "age is good", "age is bad")
validate("enter amount of pets:", 0, 4, "good job", "greate job")
