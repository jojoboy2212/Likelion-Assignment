from module import *

print("Menu")
print("1: Add")
print("2: Sub")
print("3: Multiply")
print("4: divide")
print("5: Stop")



a = calc()

while True:

    number = int(input("숫자를 입력하세요 : "))
    
    if number == 5:
        print("end")
        break
    elif number >= 5 or number <= 0:
        print("이상한 숫자 넣으면 부신다")
        continue
    else :
        num1 = int(input("첫번쨰 숫자 : "))
        num2 = int(input("두번째 숫자 : "))
        if number == 1:
            print(a.add(num1,num2))
        elif number == 2:
            print(a.sub(num1,num2))
        elif number == 3:
            print(a.mul(num1,num2))
        elif number == 4:
            print(a.div(num1,num2))


