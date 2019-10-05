# MOHAN GOPAL TRIPATHI
# IMAGINATION IS MORE IMPORTANT THAN KNOWLEDGE
#----------------------------------------------------------
# NUMEROLOGY
# SUM OF THE ALPHABETS OF THE NAME ACCORDING TO NUMEROLOGY


def number_name(characterName):
    if characterName == "A" or characterName == "J" or characterName == "S":
        return 1
    elif characterName == "B" or characterName == "K" or characterName == "T":
        return 2
    elif characterName == "C" or characterName == "L" or characterName == "U":
        return 3
    elif characterName == "D" or characterName == "M" or characterName == "V":
        return 4
    elif characterName == "E" or characterName == "N" or characterName == "W":
        return 5
    elif characterName == "F" or characterName == "O" or characterName == "X":
        return 6
    elif characterName == "G" or characterName == "P" or characterName == "Y":
        return 7
    elif characterName == "H" or characterName == "Q" or characterName == "Z":
        return 8
    elif characterName == "I" or characterName == "R":
        return 9
    else:
        print("You did something wrong")



x = raw_input("Type the name in capitals without space: ")
a = 0

for i in range(len(x)):
    y = number_name(x[i])
    a = a + y

b = str(a)
c = 0

if len(b)>1:
    for j in range(len(b)):

        c = c + int(b[j])

    #print(c)

else:
    print(a)


d = str(c)
e = 0

if len(d)>1:
    for k in range(len(d)):

        e = e + int(d[k])
    print(e)

else:
    print(c)





