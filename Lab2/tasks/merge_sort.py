import tempfile
import linecache
import random


def create_file(input_file, number_count=5000):
    with open(input_file, 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(number_count))


def write_to_file(source_file, output_file, from_pos, to_pos):
    for item in range(from_pos+1, to_pos+1):
        output_file.write(linecache.getline(source_file.name, item))


def get_digit_from_file(file, index):
    file.seek(0)
    for item, line in enumerate(file):
        if item == index:
            return int(line)


def file_len(file):
    file.seek(0)
    lines = 0
    for line in file:
        lines += 1
    return lines


def merge_sort(input_file, output):
    if file_len(input_file) >= 2:
        mid = file_len(input_file) // 2

        left = tempfile.NamedTemporaryFile('w+')
        right = tempfile.NamedTemporaryFile('w+')
        write_to_file(input_file, left, 0, mid)
        merge_sort(left, left)

        write_to_file(input_file, right, mid, file_len(input_file))
        merge_sort(right, right)
        left_index = right_index = 0
        output.seek(0)

        left_length = file_len(left)
        right_length = file_len(right)

        while left_index < left_length and right_index < right_length:
            left_number = get_digit_from_file(left, left_index)
            right_number = get_digit_from_file(right, right_index)

            if left_number < right_number:
                output.write(str(left_number) + '\n')
                left_index += 1
            else:
                output.write(str(right_number) + '\n')
                right_index += 1

        while left_index < file_len(left):
            number = get_digit_from_file(left, left_index)
            output.write(str(number) + '\n')
            left_index += 1

        while right_index < file_len(right):
            number = get_digit_from_file(right, right_index)
            output.write(str(number) + '\n')
            right_index += 1

        left.close()
        right.close()


def sort(input_file, output_file):
    with open(input_file, 'r+') as input_file:
        with open(output_file, 'w+') as output_file:
            merge_sort(input_file, output_file)
