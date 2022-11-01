# Learning python basics
# GDSC 30 days challenge

def change_case(orig_string: str):
    output = ""
    for string in orig_string:
        if string.islower():
            output += string.upper()
        if string.isupper():
            output += string.lower()
    return output


def split_in_half(orig_string: str):
    output_1 = ""
    output_2 = ""
    length = round(len(orig_string)/2)

    for x in range(int(length)):
        output_1 += orig_string[x]
    for y in range(int(length), len(orig_string)):
        output_2 += orig_string[y]
    
    return f"The first half : {output_1}\nThe second half : {output_2}"


def remove_special_characters(orig_string: str):
    special_chars = ['\'', '²', '&', 'é', '\"','(', ')', '-', '@', 'è', '_', 'ç', 'à', '=', '^', '$', '*','ù', '!', ':', ';', ',', '<', '>', '?', '.' ,'/', '§', 'µ', '£', '¨', '°', '+', '~', '€', '#', '}', '{', ']', '[', '|', '`', '\'', '¤']
    output = orig_string
    for x in output:
        if (x in special_chars):
            output.replace(x, '')

    return output
