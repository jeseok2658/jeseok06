inFp, outFp = None, None
inStr = ""

inFileName = input("소스 파일명을 입력하세요 : ")
outFileName = input("타깃 파일명을 입력하세요 : ")

inFp = open(inFileName, "r")
outFp = open(outFileName, "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("--- {} 파일이 {} 파일로 복사되었음 ---".format(inFileName, outFileName))
