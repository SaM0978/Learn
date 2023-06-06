# Regular Expressions
import re

pattern = r"[A-Z]yclone" # [] for Mathing 

text = '''Buoyed By Huge Win Against SRH, Rajasthan Royals Ready For Punjab Kings Challenge Cyclone Dyclone Jyclone
Guwahati, April 4 (PTI): Rajasthan Royals would be banking on their near-perfect combinations in almost all departments of the game to put up another commanding performance when they take on a strong Punjab Kings side in an IPL match here on Wednesday. The R'''

print(r := re.search(pattern, text))

mathes = re.finditer(pattern, text)

for match in mathes:
    print(match)
    print(text[match.span()[0]:match.span()[1]])