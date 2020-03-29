from work_with_file import read_from_file, write_list_to_file, write_dict_to_file


def get_items(file_name):
    text = read_from_file(file_name)
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "")
    return text.lower().split()


def get_words_dict(words):
    words_dict = dict()

    for item in words:
        if item in words_dict:
            words_dict[item] = words_dict[item] + 1
        else:
            words_dict[item] = 1
    return words_dict


def get_count_word_top_10(text):
    words_dict = get_words_dict(get_items(text))
    words_dict = sorted(words_dict, key=words_dict.get, reverse=True)
    write_list_to_file('Top 10: ', words_dict[:10])


def get_count_word(file_name):
    write_dict_to_file('Word count: ', get_words_dict(get_items(file_name)))
