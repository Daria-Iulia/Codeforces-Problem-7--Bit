n = int(input())
counter= 0

    
def bitz(x):
    global counter
    if x == "++X" or x == "X++":
        counter += 1
    elif x == "--X" or x == "X--":
        counter -= 1
    return counter
        
for i in range(n):
    x = str(input())
    counter = bitz(x)

print(counter)