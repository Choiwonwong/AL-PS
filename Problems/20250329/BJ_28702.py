# FizzBuzz
## 연속으로 3개의 문자열 출력, 다음에 올 문자열 출력은 어떻게될지?
# $i$가 $3$의 배수이면서 $5$의 배수이면 “FizzBuzz”를 출력합니다.
# $i$가 $3$의 배수이지만 $5$의 배수가 아니면 “Fizz”를 출력합니다.
# $i$가 $3$의 배수가 아니지만 $5$의 배수이면 “Buzz”를 출력합니다.
# $i$가 $3$의 배수도 아니고 $5$의 배수도 아닌 경우 $i$를 그대로 출력합니다.

# 이거 연속 3개가 Fizz or Buzz에 해당될 수 있나?
# 노노 3이나 5가 들어간게 문제가 아니라, 무조건 배수 여부인 것
## 이렇게 되면, 연속으로 3개가 문자일 수 있는 구조가 논리적으로 가능할까? -> 아닐 것 같음
## 즉, 3개 중에 쌩숫자인 애가 무조건 있을테니 이를 기반으로 숫자를 찾는 함수 & N4를 변환하는 함수로 나누면 될 듯?

def find_n4(n1, n2, n3):
    if n1.isnumeric():
       return int(n1) + 3 
    if n2.isnumeric():
       return int(n2) + 2 
    if n3.isnumeric():
       return int(n3) + 1

def tranform_fizzbuzz(int_value):
    if int_value % 3 == 0 and int_value % 5 == 0:
        return "FizzBuzz"
    if int_value % 3 == 0 and int_value % 5 != 0:
        return "Fizz"
    if int_value % 3 != 0 and int_value % 5 == 0:
        return "Buzz"
    else:
        return str(int_value)

N1 = input()
N2 = input()
N3 = input()

N4 = find_n4(N1, N2, N3)
print(tranform_fizzbuzz(int(N4)))