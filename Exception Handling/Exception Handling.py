try:
   num = int(input("Enter an integer: "))
   a = [6, 3]
   print(a[num])
except ValueError:
   print("Invalid input!")
except IndexError:
   print("Index out of range!")
   
print("End")

