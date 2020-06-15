def convert(number):
    numstring = ""
    if not number % 3:
        numstring += "Pling"
    if not number % 5:
        numstring += "Plang"
    if not number % 7:
        numstring += "Plong"
    if not numstring:
        numstring = "{0}".format(number)
    return numstring
