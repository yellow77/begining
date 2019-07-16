temperature = 30

if temperature > 30 :
    print("it is hot")
else:
    print("it is not hot")


name = input("put your name here ")
n = len(name)

if n <= 3 :
    print("should be more than 3 charecters")
elif n > 50 :
    print("error")
else:
    print("name looks good")


weight = int(input("your weight? "))
unit = input("please keyin (L)bs or k(G)")
if unit.upper() == "L":
    converted = weight * 0.45py
    print(f"your weight is {converted} Kilos")
else unit.upper() == "K":
    converted = weight // 0.45
    print(f"your weight is {converted} Lbs")