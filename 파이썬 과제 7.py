outFp = None
outStr = ""

fileName = input("파일명을 입력하세요 : ")

outFp = open(fileName, "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")
