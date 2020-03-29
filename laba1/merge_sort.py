from words import get_items
from work_with_file import write_list_to_file


def merge(left, right):
    sorted_arr = []
    left_index, right_index = 0, 0
    left_len, right_len = len(left), len(right)

    for item in range(left_len + right_len):
        if left_index < left_len and right_index < right_len:
            if left[left_index] <= right[right_index]:
                sorted_arr.append(left[left_index])
                left_index += 1
            else:
                sorted_arr.append(right[right_index])
                right_index += 1

        elif left_index == left_len:
            sorted_arr.append(right[right_index])
            right_index += 1

        elif right_index == right_len:
            sorted_arr.append(left[left_index])
            left_index += 1

    return sorted_arr


def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_array = merge_sort(array[: middle])
    right_array = merge_sort(array[middle: len(array) + 1])

    return merge(left_array, right_array)


def get_merge_sort(file_name):
    numbers = [int(item) for item in get_items(file_name)]
    num = merge_sort(numbers)
    write_list_to_file('Merge sort: ', num)
