def word_histogram(str):
    dict = {}
    list_of_str = str.split()
    for word in list_of_str:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    print(dict)