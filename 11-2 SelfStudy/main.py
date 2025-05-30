inFp = None
inList, inStr = [], ""

inFp = open("CookBook.txt", "r")

inList = inFp.readlines()
for i in inList:
    print("%d : %s (i+1, inList)", end = "")

inFp.close()
