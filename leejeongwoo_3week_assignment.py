# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    # your code
    return "next"

# 문제 2번
def leapYear(year):
    # your code
    if year%4==0 and year%100!=0 :
        return "윤년입니다."
    elif year%400==0:
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."

# 문제 3번
def alram(time):
    # your code
    if 0<=time<45:
        return "오후 23시 "+str(time+15)+"분"
    elif 45<=time<100:
        return "오전 0시 "+str(time-45)+"분"
    elif 100<=time<1000:
        x=str(time)
        hour=int(x[0:1])
        min=int(x[1:])
        min1=min-45
        if min1<0:
            hour=hour-1
            min1=60+min1
        return "오전 "+str(hour)+"시 "+str(min1)+"분"
    elif 1000<=time<1245:
        x=str(time)
        hour=int(x[0:2])
        min=int(x[2:4])
        min1=min-45
        if min1<0:
            hour=hour-1
            min1=60+min1
        return "오전 "+str(hour)+"시 "+str(min1)+"분"
    elif 1245<=time<2359:
        x=str(time)
        hour=int(x[0:2])
        min=int(x[2:4])
        min1=min-45
        if min1<0:
            hour=hour-1
            min1=60+min1
        return "오후 "+str(hour)+"시 "+str(min1)+"분"
    
     

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    # your code
    z=((x1-x2)**2+(y1-y2)**2)**(1/2)
    if x1==x2 and y1==y2:
        if r1==r2!=0:
            return "어딘지 모르겠다 오바"
        elif r1==r2==0:
            return 1
        elif r1!=r2:
            return  0              
    else:
        if z>r1+r2:
            return 0
        elif z==r1+r2:
            return 1
        elif r2==z+r1 or r1==z+r2:
            return 1
        elif r1>z+r2 or r2>z+r1:
            return 0 
        else:
            return 2


