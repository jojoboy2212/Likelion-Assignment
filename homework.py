'''
과제1-1
while문을 활용하여 1부터 1000까지의 자연수 중 3의 
배수의 합을 구해보세요
'''
print("과제1-1")
num = 0
threeVar = 0
while num < 1001:
    num += 1
    if num%3 ==0:
        threeVar += num
        if num == 1000:
            break
print(threeVar)    


'''
과제 1-2
while문을 활용하여 아래와 같이 *을 출력하는프로그램을 만들어 보세요
**********
*********
********
*******
******
*****
****
***
**
*
'''
print("과제1-2")
star = 11
while star >= 0:
    star -= 1
    star1 = '*'*star
    if star == 0:
        break
    print(star1)



'''
과제1-3
다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점
이상의 점수들의 총 합을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
'''
print("과제1-3")
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i >= 50:
        sum += i   
print(sum)


'''
과제2-1
for문을 활용하여 1부터 100까지의 숫자를 출력해보세요
'''
print("과제2-1")
num = range(1, 101, 1)
for nums in num:
    if nums == 101:
        break
    print(nums)

'''
과제2-2
for문을 활용하여 A학급의 평균 점수를 구해보세요
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
'''
print("과제2-2")
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for num in range(len(A)):
    total += A[num]
avg = total / len(A)
print(avg)

'''
과제2-3
리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다.
다음 코드를 리스트 내포를 이용하여 표현하세요.
numbers = [1,2,3,4,5]

result = []
for n in numbers:
    if n % 2 ==1:
        result.append(n*2)
'''
print("과제2-3")
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)

'''
연습문제1
'''
print("연습문제1")
new_list = ['Life', 'is', 'too', 'short']
print(" ".join(new_list))

'''
연습문제2
'''
print("연습문제2")
mut = 'mutzangesazachurum'
count = 0
for i in mut:
    if i in 'aeiou':
        count += 1
print(count)