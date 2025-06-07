from PIL import Image
import tkinter as tk
from tkinter import messagebox

경로1 = "이미지.jpg"
경로2 = "이미지 1.jpg"
경로3 = "이미지 (1).jpg"
경로4 = "이미지 1 (1).jpg"
경로5 = "이미지 2.jpg"
경로6 = "이미지 4.jpg"
경로7 = "이미지 3.jpg"
경로8 = "이미지 5.jpg"

fixed_phrases = [
    "나여 백종원!",
    "이건 우리 짬뽕이 아니에유",
    "우리 농가 살려야쥬",
    "대패삼겹살도 제가 처음 개발한 거에유",
    "브라질 농가 살려야쥬",
    "한 근 500그람 아니에유?",
    "역사는 빽햄 이전과 이후로 기록될 것입니다",
    "어묵을 넣지 말란 법이 있을까?"
]

photo_map = {
    fixed_phrases[0]: 경로1,
    fixed_phrases[1]: 경로2,
    fixed_phrases[2]: 경로3,
    fixed_phrases[3]: 경로4,
    fixed_phrases[4]: 경로5,
    fixed_phrases[5]: 경로6,
    fixed_phrases[6]: 경로7,
    fixed_phrases[7]: 경로8
}

root = tk.Tk()
root.withdraw()

user_input = input("한 마디 해봐유~: ")

if user_input in photo_map:
    img = Image.open(photo_map[user_input])
    img.show()
    
    answer = messagebox.askyesno("사진 더 보기", "다른 사진들도 보실래유?")
    
    if answer:  
        for phrase in fixed_phrases:
            if phrase != user_input:
                img = Image.open(photo_map[phrase])
                img.show()
    else:
        print("아쉽지만 다음에 또 봐유!")
else:
    print("에이~ 그 말은 우리 프로그램에 없네유!")
