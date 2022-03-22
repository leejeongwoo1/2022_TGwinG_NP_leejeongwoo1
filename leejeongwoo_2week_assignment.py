# 문제 1번
def sum(a,b):
    # your code
    return (a+b)
print(sum(3,4))
# 문제 2번
def sub(a,b):
    # your code
    return (a-b)
print(sub(3,2))
# 문제 3번
def mul(a,b):
    # your code
    return (a*b)
print(mul(3,2))
# 문제 4번
def div(a,b):
    # your code
    return (a/b)
print(div(32,3))
# 문제 5번
def distance(x1,y1,x2,y2):
    # your code
    return (((x1-x2)**2+(y1-y2)**2)**1/2)
print(distance(2,1,5,4))
# 문제 6번
def short():
    lylic = "life is short art is long"
    # your code
    return (lylic[8:13])
print(short())
# 문제 7번
def myReverse(string):
    # your code
    return (string[::-1])
print(myReverse("Hello"))
# 문제 8번
def letMeIntroduceMyself():
    # your code
    A=input("이름을 입력하십시오:") 
    B=input("취미를 입력하시오:")
    C=input("재학 중인 대학을 입력하시오:")
    D=input("생일을 입력하시오(예시030901):")
    E=int(D[2:4])
    F=int(D[4:6])
    print("제 이름은 {0} 입니다. 제 취미는 {1}이구요. 저는 {2}를 다니고 있습니다. 제 생일은 {3}월 {4}일 입니다.".format(A, B, C, E, F))
    return "제 이름은 {0} 입니다. 제 취미는 {1}이구요. 저는 {2}를 다니고 있습니다. 제 생일은 {3}월 {4}일 입니다.".format(A, B, C, E, F)
letMeIntroduceMyself()
# 문제 9
def calcAI():
    # your code
    A= int(input("첫 번째 숫자를 입력하시오:"))
    B=int(input("두 번째 숫자를 입력하시오:"))
    C=sum(A,B)
    print("두 수의 합은 {0} 입니다".format(C))
    return "두 수의 합은 {0} 입니다".format(C)
calcAI()