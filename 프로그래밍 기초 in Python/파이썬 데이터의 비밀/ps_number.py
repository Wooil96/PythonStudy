# def mask_security_number(security_number):
#     # 코드를 입력하세요.
#     new_mask_security_number = list(security_number)
#     security_number = ""

#     for x in range(-4, 0) :
#         new_mask_security_number[x] = "*"
        
#     for y in range(len(new_mask_security_number)):
#         security_number += new_mask_security_number[y]
    
#     return security_number

def mask_security_number(security_number):
    return security_number[:-4] + '****'

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))