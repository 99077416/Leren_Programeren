
def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator)
    if 0 <= position< len(splitted_strings):
        value = splitted_strings[position]
    else:
        value = None
    return value

print(get_value('muis,kat,hond', ',' ,1))
