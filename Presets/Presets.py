from re import X

import Functions

from math import sqrt as square_root

def square(n):
    '''Square Finder'''
    print(f"Square of {n} is",n**2)

def Subtraction(FirstValue,MidValue=0,TotalValue=0):   
     if FirstValue == X:
         K = int(TotalValue)-int(MidValue)
         print("The Value Of X =",K)
         exit()        
     if MidValue == X:
         K = int(TotalValue)-int(MidValue)
         print("The Value Of X =",K)
         exit()        
     if TotalValue == X:
         K = int(MidValue)-int(FirstValue)
         print("The Value Of X =",K)
         exit()        
     elif FirstValue and MidValue and TotalValue != 0:
         K = int(TotalValue)-int(MidValue)-int(FirstValue)
         print("All Value Subtracted Together are =",K)
         exit()
     else:
         K = int(FirstValue)-int(MidValue)
     print("First Value - Mid Value =",K) 

def Addtion(FirstValue,MidValue,TotalValue=0):
     if FirstValue == X:
         K = int(TotalValue)+int(MidValue)
         print("The Value Of X =",K)
         exit()        
     if MidValue == X:
         K = int(TotalValue)+int(MidValue)
         print("The Value Of X =",K)
         exit()        
     if TotalValue == X:
         K = int(MidValue)+int(FirstValue)
         print("The Value Of X =",K)
         exit()        
     elif FirstValue and MidValue and TotalValue != 0:
         K = int(TotalValue)+int(MidValue)+int(FirstValue)
         print("All Value Added Together are =",K)
         exit()
     else:
         K = int(FirstValue)+int(MidValue)
     print("First Value - Mid Value =",K) 

def Name_Checker(F = "",G="",H=""):
    Name = input("Enter Your Name?\n").capitalize()
    if Name in["Samad","Hussain","Zainab",F,G,H]:
        Evil_Status = input("Are You Evil?\n").capitalize()
        if Evil_Status in ["Yes"]:
            Good_Deeds = input("How Many Good Deeds Did You Do Today?\n")
            Good_Deeds = int(Good_Deeds)
            if Good_Deeds > 7:
                print("You Are Allowed")
            else:
                print("You Can't Enter")
        elif Evil_Status in["No"]:
            print("You Are Welcomed")       
        else:
            print("?????")    
    else:
        print("1")

def function_maker(F=0):
    func_name = input("Name of the function: ")
    
    def new_function(H=0):
        print("Your function is ready")
        if H > 100000000000000:
            print("f")
    
    new_function.__name__ = func_name
    print(f"def {func_name}(H=0):")
    return new_function


def Name_Checker(H=""):
    Name = input("Enter Your Name?\n").capitalize()
    if Name in ["Samad", "Hussain", "Zainab",H]:
        Evil_Status = input("Are You Evil?\n").capitalize()
        if Evil_Status in ["Yes"]:
            Good_Deeds = input("How Many Good Deeds Did You Do Today?\n")
            Good_Deeds = int(Good_Deeds)
            if Good_Deeds > 7:
                print("You Are Allowed")
            else:
                print("You Can't Enter")
        elif Evil_Status in ["No"]:
            print("You Are Welcomed")
        else:
            print("?????")
    else:
        print("You Are Heatily Welcomed in Our Cafe", Name)
    return Name


def table():
    a = int(input("Enter The Number: "))

    print(f"Multiplication Table of {a} is: ")

    for i in range(1, 11):
        print(f"{a} X {i} = {a*i}")

def Square_Root():
    Number = int(input('Enter The Number You Wanna Square Root\n'))
    Square_Root = square_root(Number)
    print(f'Square Root of {Number} is {Square_Root:.2f}')

if __name__ =="__main__":

 table()
