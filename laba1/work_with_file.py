FILE_OUTPUT = 'output'
FILE_INPUT = 'file'


def read_from_file(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    return text


def write_dict_to_file(text, some_dict, file_name=FILE_OUTPUT):
    with open(file_name, 'w') as file:
        file.write(text+'\n')
        for item in some_dict:
            file.write(f'{item} - {some_dict[item]}\n')


def write_list_to_file(text, some_list, file_name=FILE_OUTPUT):
    with open(file_name, 'w') as file:
        file.write(text + '\n')
        for item in some_list:
            file.write(f'{item} ')
