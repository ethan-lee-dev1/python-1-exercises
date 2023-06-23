def calc_total(list, tax):
    total = 0
    for num in list:
        total += num
    taxStr = ""
    for char in tax:
        if char.isdigit():
            taxStr += char
    result = total + (total * float(taxStr) * 0.01)
    result = "${:,.2f}".format(result)
    print(result)