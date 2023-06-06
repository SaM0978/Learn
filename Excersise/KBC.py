print("Welcome To Kaun Banega Crorepati!!")

print("So Your First Ques For 41000 is:")

print("Who Invented Small Pox Vaccine?: ")

print("Option-1 Hussain")
print("Option-2 Edward Jenner")
print("Option-3 Uchiha Sasuke")
print("Option-4 KS Sivan")

Ans_1 = input()

if Ans_1 == "2":
    print("Congrats You Just Won 41000 Rupees!!!")
    Total = 4100
else:
    print("Opps You Chose The Wrong Answer")

print("\nWho Died in 1234?: ")

print("Option-1 Naruto")
print("Option-2 You")
print("Option-3 Me")
print("Option-4 Baha ad-Din ibn Shaddad ")

Ans_Second = input()

if Ans_Second == "4":
    print("Congrats You Won 8900 Rupees")
    Total = 13000
elif Ans_1 == "2" and Ans_Second == "4":
    print("You Got Both The Answers Correct Won You Over 9000 Rupees")

print("\nWho Died in 1545?: ")

print("Option-1 Sher Shah Suri")
print("Option-2 Kalia")
print("Option-3 Mughal")
print("Option-4 Goku")

Ans_Third = input()

if Ans_Third == "1":
    print("Congrats You Won 10000 Rupees!!!")
    Total = 23000
else:
    print("Opps Wrong Answer (:")

if Ans_Third == "1" and Ans_1 == "2" and Ans_Second == "4":
 Total = 23000
 print("Your Grand Total Is",str(Total))
