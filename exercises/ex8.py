def f_to_c(f):
    c = (f - 32) * (5/9)
    c = round(c)
    print(f"{f} degress Fehrenheit is {c} degrees in Celcius")
def c_to_f(c):
    f = (c * (9/5)) + 32
    f = round(f)
    print(f"{c} degress Celcius is {f} degrees in Fahrenheit")