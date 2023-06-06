# # Decotarter is Fuction Modifer


# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks For Using This Fuction!!")
#     return mfx   

# @greet
# def hello():
#     print("hello world".capitalize())

# @greet
# def add(a, b):
#     print(f"{a + b}")

# hello()

def Abdus(fx):
    def mfx(*args, **kwargs):
        print("Sus")
        fx(*args, **kwargs)
    return mfx


@Abdus
def add(a, b):
    print(f"Added Value Is {a + b}")


add(3,5)

















