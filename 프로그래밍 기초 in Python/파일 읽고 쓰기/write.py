import os

print(os.getcwd()) #
os.chdir('K:\\Python Group Study\\프로그래밍 기초 in Python\\파일 읽고 쓰기') # 절대 경로를 이 프로그래밍이 실행 된 후 바꿔준다. 프로그램이 끝나면 원상복구 됌

print(os.getcwd())

"""
파일 다루기에는 총 6가지가 존재한다.
r : 읽기 모드 : 파일을 읽기만 할 때 사용(파일 없으면 에러)
r+ : 읽기 or 쓰기 모드(파일이 없으면 에러) => 기존 파일에 있던 데이터를 그대로 두고 그 위에 내용을 덮어쓴다.
w : 쓰기모드 : 파일에 내용을 입력할 때 사용(파일이 없으면 생성)
w+ : 읽기 or 스기 모드(파일이 없으면 생성) => 기존 파일에 있던 데이터를 완전히 지우고 새로 내용을 입력한다.
a : 추가모드(append) : 파일의 마지막에 새료운 내용을 추가할 때 사용(파일이 없으면 생성)
a+ : 읽기 or 추가 모드(파일이 없으면 생성) => 기존 파일에 있던 데이터를 그대로 두고 마지막에 내용을 입력한다.
"""

# with open('new_file.txt', 'w') as f:
#     f.write("Hello world!\n")
#     f.write("My name is Healy")


with open('new_file.txt', 'w') as f:
    f.write("ABCD\n")
    

# with open('new_file.txt', 'a') as f:
#     f.write("This is Append\n")
    