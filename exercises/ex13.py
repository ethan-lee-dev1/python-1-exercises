def frame_it(list_of_words):
    max_length = 0
    for word in list_of_words:
        if max_length < len(word):
            max_length = len(word)
    print("*" * (max_length + 4))
    for word in list_of_words:
        padding = " " * (max_length - len(word))
        print(f"* {word}{padding} *")
    print("*" * (max_length + 4))
