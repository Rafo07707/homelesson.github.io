what = input ("Ընտրեք Գործողությունը (+,-,/,*)? ; ")

a=float(input("Ներմուծեք 1-ին թիվը։ "))
b=float(input("Ներմուծեք 2-րդ թիվը։ "))

if what == "+":
    c = a + b 
    print("Արդյունք։ "+str(c))
elif what == "-":
    c = a - b
    print("Արդյունք։ " +str(c))
elif what == "/":
    c = a / b
    print("Արդյունք։ " +str(c))
elif what == "*":
    c = a * b
    print("Արդյունք։ " +str(c))   
else:
    print("EROR")