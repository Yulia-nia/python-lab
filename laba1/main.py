import argparse
from fibonacci import get_fibonacci
from merge_sort import get_merge_sort
from quick_sort import get_quick_sort
from words import get_count_word, get_count_word_top_10


parser = argparse.ArgumentParser(prog='Lab 1')
parser.add_argument('-m', '--method')
parser.add_argument('-f', '--file')
parser.add_argument('argument_list', nargs=argparse.REMAINDER)


if __name__ == '__main__':
    args = parser.parse_args()
    file_name = args.file

    if args.method == 'fibonacci':
        get_fibonacci(int(args.argument_list[0]))
    elif args.method == 'top':
        get_count_word_top_10(file_name)
    elif args.method == 'merge':
        get_merge_sort(file_name)
    elif args.method == 'quick':
        get_quick_sort(file_name)
    elif args.method == 'word_count':
        get_count_word(file_name)
