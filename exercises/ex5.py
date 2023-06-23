def replace_period(sentence, punctuation):
    str = ""
    for char in sentence:
        if char == ".":
            str += "!"
        else:
            str += char
    print(str)