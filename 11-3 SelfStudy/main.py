import os

ouFp = None
ourStr = ""
filename = "CookBook.txt"

ouFp = open(filename, "w")

while True:
    ourStr = input("입력 : ")
    if ourStr != "":
        ouFp.writelines(ourStr + "\n")
        
    else:
        break

ouFp.close()

print("파일명 :" + filename)
print("파일 내용:")
os.system(f'type "{filename}"')
