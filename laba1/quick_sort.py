from words import get_items
from work_with_file import write_list_to_file


def sort_quick(array):
    if len(array) < 2:
        return array
    else:
        start_number = array[0]
        left_array, right_array = [], []

        for item in array[1:]:
            if item <= start_number:
                left_array.append(item)

        for item in array[1:]:
            if item > start_number:
                right_array.append(item)

        return sort_quick(left_array)+[start_number]+sort_quick(right_array)


def get_quick_sort(file_name):
    numbers = [int(item) for item in get_items(file_name)]
    num = sort_quick(numbers)
    write_list_to_file('Quick sort: ', num)
