def diagonal_printer(str):
    list_of_str = str.split()
    for i in range(len(list_of_str)):
        result = ""
        for str in list_of_str[i]:
            for i in range(len(str)):
                result += " "
                print(result + str)