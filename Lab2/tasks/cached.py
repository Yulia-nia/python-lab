def cached_func(function):
    memo = dict()

    def func(*args):
        value = memo.get(args, None)
        if value is None:
            result = function(*args)
            memo[args] = result
            return result
        return value

    return func


@cached_func
def fact(number):
    if number == 1 or number == 0:
        return 1
    return number * fact(number - 1)


