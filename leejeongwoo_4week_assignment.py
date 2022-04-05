# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번
def intervention(queue):
    answer = list()  
    # your code 
    if ('성은' in queue)==True and queue.index('성은')>=4:
        queue.insert(queue.index('성은')+1,'승호')
        answer=queue
    elif ('성은' in queue)==True and queue.index('성은')<4:
        queue.append('승호')
        answer=queue
    else:
        queue.append('승호')
        answer=queue
    return answer

# 문제 2번
def pascal(n):
    answer = list()
    # your code      
    x=[]
    for i in range(n):
        from math import factorial
        x.append(int(factorial(n-1)/(factorial(i)*factorial(n-i-1))))
    answer=x      
    return answer

# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    x=len(searchWords)
    p=len(entry)
    z=[]
    for i in range(x):
        y=len(searchWords[i])
        for l in range(y-(p-1)):
            if searchWords[i][l:l+p]==entry:
                z.append(searchWords[i])
            else:
                continue
    z.sort()
    answer=z
    # your code
    return answer

# 문제 4번
def stock_price(stockChart):
    answer = str()
    # your code
    z=[]
    b=0
    x=[]
    m=1
    for i in stockChart:
        b=b+(i)
        z.append(b)
    for v in z[:-1]:
        L=z[-1]-v
        x.append(L)
    for q in range(len(x)):
        if max(x)==x[q]:
            m=q
    if max(x)>0:
        answer=str(len(x)-m)+"일 전에 샀어야지 으이구"
    else:
        answer="아니야 조금만 더 기다려"
    return answer

# 문제 5번
def decryption(letter):
    answer = str()
    # your code
    k='1'
    def abc(x):
        if x=='a':
            x='x'
        if x=='b':
            x='y'
        if x=='c':
            x='z'
        if x=='d':
            x='a'
        if x=='e':
            x='b'
        if x=='f':
            x='c'
        if x=='g':
            x='d'
        if x=='h':
            x='e'
        if x=='i':
            x='f'
        if x=='j':
            x='g'
        if x=='k':
            x='h'
        if x=='l':
            x='i'
        if x=='m':
            x='j'
        if x=='n':
            x='k'
        if x=='o':
            x='l'
        if x=='p':
            x='m'
        if x=='q':
            x='n'
        if x=='r':
            x='o'
        if x=='s':
            x='p'
        if x=='t':
            x='q'
        if x=='u':
            x='r' 
        if x=='v':
            x='s'
        if x=='w':
            x='t' 
        if x=='x':
            x='u' 
        if x=='y':
            x='v' 
        if x=='z':
            x='w'    
        else:
            x=x
        return x
    for i in range(len(letter)):
        k=k+abc(letter[i])
    answer=k[1:]
    return answer

