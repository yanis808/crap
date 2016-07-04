# Program calculator. The calculator can calculate basic operations like +, -, /, * with two positive numbers.
# Please separate numbers and operators with withe space.
start = input("Co chcesz obliczyć?\n")
while start != "":
    part = start.split()
    if part[1] == "+":
        score = int(part[0]) + int(part[2])
        print(score)
    elif part[1] == "-":
        score = int(part[0]) - int(part[2])
        print(score)
    elif part[1] == "/":
        if int(part[2]) == 0:
            print("Dzielenie przez 0 nie jest możliwe")
        else:
            score = int(part[0]) / int(part[2])
            print(score)
    elif part[1] == "*":
        score = int(part[0]) * int(part[2])
        print(score)
    start = input("Co chcesz obliczyć?\n")
print("Koniec")