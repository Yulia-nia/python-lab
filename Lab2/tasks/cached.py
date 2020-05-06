def cached_func(function):
    memo = dict()

    def func(*args):
        if args not in memo:
            memo[args] = function(*args)
        return memo[args]

    return func


@cached_func
def fact(number):
    if number == 1 or number == 0:
        return 1
    return number * fact(number - 1)
