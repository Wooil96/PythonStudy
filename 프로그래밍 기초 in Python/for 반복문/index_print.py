numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 코드를 입력하세요.
a = 0
for i in numbers :
    print(f"{a}" + " " + f"{i}")
    a += 1

# Answer #
for i in range(len(numbers)):
    print(i, numbers[i])