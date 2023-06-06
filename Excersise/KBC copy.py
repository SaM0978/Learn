Correct_Answer =["2","4","1",]

print("Welcome To Kaun Banega Crorepati!!")

print("So Your First Ques For 41000 is:")

print("Who Invented Small Pox Vaccine?: ")

print("Option-1 Hussain")
print("Option-2 Edward Jenner")
print("Option-3 Uchiha Sasuke")
print("Option-4 KS Sivan")

Ans_1 = input()

if Ans_1 == Correct_Answer[0]:
    print("Congrats You Just Won 41000 Rupees!!!")
    Total_1 = 4100
    Answer_1 = "Correct"
else:
    print("Opps You Chose The Wrong Answer")

print("\nWho Died in 1234?: ")

print("Option-1 Naruto")
print("Option-2 You")
print("Option-3 Me")
print("Option-4 Baha ad-Din ibn Shaddad ")

Ans_Second = input()

if Ans_Second == Correct_Answer[1]:
    print("Congrats You Won 8900 Rupees")
    Total_2 = 13000
    Answer_2 = "Correct"
elif Ans_1 == Correct_Answer[0] and Ans_Second == Correct_Answer[1]:
    print("You Got Both The Answers Correct Won You Over 9000 Rupees")

print("\nWho Died in 1545?: ")

print("Option-1 Sher Shah Suri")
print("Option-2 Kalia")
print("Option-3 Mughal")
print("Option-4 Goku")

Ans_Third = input()

if Ans_Third == Correct_Answer[2]:
    print("Congrats You Won 10000 Rupees!!!")
    Total_3 = 23000
    Answer_3 = "Correct"
else:
    print("Opps Wrong Answer (:")
if Ans_1 == Correct_Answer[0] and Ans_Second == Correct_Answer[1] and Ans_Third == Correct_Answer[2]:
 Total = 23000
 print("Your Grand Total Is",str(Total))
else:
    l = 4 
if Answer_1 and Answer_2 and Answer_3 in["Correct"]:
    print(int(Total_1)+int(Total_2))