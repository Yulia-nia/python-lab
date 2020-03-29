from work_with_file import write_list_to_file


def fibonacci(number):
    if number < 2:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def get_fibonacci(number):
    array = []
    for item in range(number):
        array.append(fibonacci(item))
    write_list_to_file('Fibonacci: ', array)

