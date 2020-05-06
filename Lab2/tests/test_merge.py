import tasks.merge_sort as merge


def test_sort_file():
    input_file = "input.txt"
    output_file = "output.txt"

    merge.create_file(input_file)
    merge.sort(input_file, output_file)


if __name__ == '__main__':
    test_sort_file()
