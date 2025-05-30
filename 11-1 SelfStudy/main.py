inFp = None
inStr = ""

inFp = open("CookBook.txt", "r", )

for i in range(1, 4):
    inStr = inFp.readline()
    if not inStr:
        break
    print("%d : %s" % (i, inStr), end = "")

inFp.close()
