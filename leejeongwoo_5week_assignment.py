# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점
import math
from re import X
def calcCircleArea(r):
    result = float()
    '''[2]'''
    result="%0.2f" % (math.pow(r,2)*math.pi)
    return result
def calcLog(a, b):
    result = float()
    '''[3]'''
    result="%0.2f" %(math.log(b,a))
    return result
def calcSin(x):
    result = float()
    '''[4]'''
    result="%0.2f" %(math.sin(x))
    return result
def calcFactorial(x):
    result = int()
    '''[5]'''
    result=int(math.factorial(x))
    return result
def calcCombination(n, r):
    result = int()
    '''[6]'''
    result=int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
    return result

def calculator(order):
    answer = 0
    '''[1]'''
    if "원넓이" in order:
        answer=calcCircleArea(float(order[5:]))
    elif '로그'in order:
        if 'e' in order:
            a=order.split()
            answer=calcLog(math.e,float(a[2]))
        else:
            b=order.split()
            answer=calcLog(float(b[1]),float(b[2]))
    elif "사인"in order:
        answer=calcSin(float(order[4:]))
    elif "팩토리얼"in order:
        answer=calcFactorial(int(order[6:]))
    elif "조합"in order:
        c=order.split()
        answer=calcCombination(int(c[1]),int(c[2]))
    return answer