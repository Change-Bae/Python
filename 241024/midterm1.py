# 3주차 1번
# a = int(input('첫 번째 숫자를 입력하시오 : '))
# b = int(input('두 번쨰 숫자를 입력하시오 : '))

# print(a > 0 and b > 0)

# 2번
# a = input('첫 번째 문자열을 입력하시오 : ')
# b = input('두 번째 문자열을 입력하시오 : ')

# print(a == b)

# 3번
# money = int(input('지폐로 교환할 돈은 얼마? : '))
# a = money // 50000
# b = (money - a * 50000) // 10000
# c = (money - a * 50000 - b * 10000) // 5000
# d = (money - a * 50000 - b * 10000 - c * 5000) // 1000
# e = money - a * 50000 - b * 10000 - c * 5000 - d * 1000

# print('5만원 ->', a, '장')
# print('1만원 ->', b, '장')
# print('5천원 ->', c, '장')
# print('1천원 ->', d, '장')
# print('나머지 ->', e , '원')

# 4번
# a, b, c = map(int, input('숫자를 입력하시오 : ').split())
# aver = (a + b + c) // 3

# print(int(a > b and a > c), end=' ')
# print(int(a == b ==c), end=' ')
# print(aver)

# 5번
total = 2000
x = 2000 // 1.28
print('직접비 :', int(x),'만원')
print('간접비 : ', int(total - x),'만원')