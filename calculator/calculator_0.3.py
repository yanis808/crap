# Program calculator. The calculator can calculate basic operations like +, -, /, * with two positive numbers.
# You don't need separate numbers and operators with withe space.
# In this version is possible to calculate more than 2 numbers.
start = input("Co chcesz obliczyć?\n")
while start != "":
    if "+" in start:
        part = start.split("+")
        score = int(part[0]) + int(part[1])
        print(score)
    elif "-" in start:
        part = start.split("-")
        score = int(part[0]) - int(part[1])
        print(score)
    elif "/" in start:
        part = start.split("/")
        if int(part[1]) == 0:
            print("Dzielenie przez 0 nie jest możliwe")
        else:
            score = int(part[0]) / int(part[1])
            print(score)
    elif "*" in start:
        part = start.split("*")
        score = int(part[0]) * int(part[1])
        print(score)
    start = input("Co chcesz obliczyć?\n")
print("Koniec")
