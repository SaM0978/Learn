def function():
    try:
        l = [5, 6, 3,  8]
        i = int(input("Enter The Index: "))
        print(l[i])
    except:
        print("Some Error Occurred")
    finally:
        print("I Am Inevitable") 
    return "Over"

x = function()

print(x)

# in def finally required
