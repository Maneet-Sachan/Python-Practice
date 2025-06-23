computer= random.choice([1,-1,0])
youstr= input("enter your choice:")
youdict = ("s" : 1, "g" : -1, "w" : 0 )
reversedict = ("snake" : 1, "water" : 0, "gun" : -1)

you= youdict[youstr]
print(f"you chose {reversedict[you]}/computer chose {reversedict[computer]}")
