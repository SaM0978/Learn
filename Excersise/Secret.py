import random
import clipboard

def encode_string(a):
    if len(a) == 3:
        random_choice = random.choice(["avd", "hry", "sfb"])
        fixed = a[0]
        letter_1 = a[1]
        letter_3 = a[2]
        String = random_choice + letter_1 + letter_3 + fixed + random_choice
        return String
    elif len(a) == 2:
        fixed = a[0]
        letter_1 = a[1]
        String = letter_1 + fixed
        return String
    elif len(a) > 3:
        random_choice = random.choice(["avd", "hry", "1sfb"])
        fixed = a[0]
        letter_1 = a[1]
        letter_last = a[-1]
        random_last = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        middle_letters = a[2:-1]
        String = random_choice + letter_1 + middle_letters + letter_last + fixed + random_last
        return String
    else:
        return "Error: Invalid input string length"

def decode_string(a):
    if len(a) == 2:
        fixed = a[1]
        letter_1 = a[0]
        String = fixed + letter_1
        return String
    elif len(a) == 9:
        Random_1 = a[0]
        Random_2 = a[1]
        Random_3 = a[2]
        Letter_1 = a[3]
        Letter_2 = a[4]
        Letter_3 = a[5]
        Random_last_1 = a[6]
        Random_last_2 = a[7]
        Random_last_3 = a[8]
        String = Letter_2 + Letter_3 + Letter_1
        return String
    elif len(a) > 9:
        Random_1 = a[0]
        Random_2 = a[1]
        Random_3 = a[2]
        Middle_Letters = a[3:-3]
        Random_last_1 = a[-3]
        Random_last_2 = a[-2]
        Random_last_3 = a[-1]
        String = Middle_Letters[-1] + Middle_Letters[:-1] 
        return String
    else:
        return "Error: Invalid input string length"

C = input("Code or Decode\n")

if C in ['Code', '1']:
    a = input('Enter The String You Wanna Code\n')
    encoded_string = encode_string(a)
    clipboard.copy(encoded_string)
    print("Encoded string:", encoded_string)
else:
    a = input("Enter The String You Wanna Decode\n")
    decoded_string = decode_string(a)
    print("Decoded string:", decoded_string)
