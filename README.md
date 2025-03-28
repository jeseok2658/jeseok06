select = int(input("입력할 진수 결정하기(16/10/8/2):")
a = input("값 입력")

if select == 16 :
                   b=int(a, 16)
if select == 10 :
                   b=int(a, 10)
if select == 8 :
                   b=int(a, 8)
if select == 2 :
                   b=int(a,2)

print("16진수 ==>", hex(b))
print("10진수 ==>", b)
print("8진수 ==>", oct(b))
print("2진수 ==>", bin(b))
