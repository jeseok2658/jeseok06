inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r")  
inList = inFp.readlines()              

for i, inStr in enumerate(inList):     
    print(f"{i+1}: {inStr}", end="")   

inFp.close()  
