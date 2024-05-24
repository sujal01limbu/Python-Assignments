# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,


def print_pattern(n):

    
    for i in range(1, n + 1):
        print('*' * i)


input_number = 3
print_pattern(input_number)
