# 2.Write a python program
# to find max of two
# numbers. 

# def maxsimum(a,b):
#     if a > b:
#         return a
#     else:
#         return b    

# a = 2 
# b = 4
# print(maxsimum(a, b))
  
# 3.Write a python program to sum all numbers.

# total = 0 
# list1 =[11,2,12,5,7,9,10]
# for ele in range(0,len(list1)):
#     total = total + list1[ele]
# print("tvyal tveri gumary havasar e " , total)


#1 Kalkulator 

def gum(x,y):
    return x + y 

def han(x,y):
    return x - y 

def bazm(x,y):
    return x * y 

def baj(x,y):
    return x / y

print("Select operation.")
print("1.gumarum")
print("2.hanum")
print("3.bazmakatkum")
print("4.bajanum")

while True:
    choice = input("nermuceq gorcoxutyun (1/2/3/4) ")
    if choice in ('1','2','3','4'):
        num1 = float(input("Nermuceq 1 tivy "))
        num2 = float(input("Nemuceq  2 tivy "))
        if choice == '1':
            print(num1,"+", num2 ,"=", gum(num1, num1))
        elif choice == '2':
             print(num1,"-", num2 ,"=", han(num1, num1))
        elif choice == '3':
             print(num1,"*", num2 ,"=", bazm(num1, num1))     
        elif choice == '4':
             print(num1,"/", num2 ,"=", baj(num1, num1))