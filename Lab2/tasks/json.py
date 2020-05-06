def json_convert(value):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        return f"\"{value}\""

    if isinstance(value, (list, tuple)):
        string_result = ', '.join(map(json_convert, value))
        return "[" + string_result + "]"

    if isinstance(value, dict):
        if not all(isinstance(key, (str, int, float, bool, type(None))) for key in value.keys()):
            raise TypeError('Key in dictionary is not serializable')

        dict_keys = list(map(str, value.keys()))
        dict_values = list(value.values())
        string_result = ", ".join(f"{json_convert(key)}: {json_convert(dict_value)}"
                                   for key, dict_value in zip(dict_keys, dict_values))

        return "{" + string_result + "}"

    raise TypeError("Object is not serializable")
