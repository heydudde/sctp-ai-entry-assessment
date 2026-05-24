def convertTemp(value, unit):
    if unit == "C":
        result = (value * 9 / 5) + 32
    elif unit == "F":
        result = (value - 32) * 5 / 9
    else:
        return -1

    return round(result, 2)


print(convertTemp(100, "C"))
print(convertTemp(32, "F"))
print(convertTemp(37, "C"))
print(convertTemp("invalid", "X"))