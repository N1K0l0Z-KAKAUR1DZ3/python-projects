name = "nika kakauridze"
i = 0
for char in name:
    if char not in " aeiou":

        print("tanxmovani detected at position", i, char)
        i+=1

    elif char in "aeiou":
        print("xmovani detected at position", i, char)

    else:
        
        print("")
