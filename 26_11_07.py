#가위 바위 보
def solution(rsp):
    answer=""
    for x in rsp:
        if x=="0":
            answer=answer+"5"
        if x=="2":
            answer=answer+"0"
        if x=="5":
            answer=answer+"2"
    return answer
    
  #Common multiples
    def solution(number, n, m):
    answer = 0
    if number%n==0 and number%m==0:
        answer=1
    elif number%n==1 or number%m==1:
        answer=0
    return answer
  
#Finding divisors
def solution(n):
    answer = []
    for x in range(1,n+1):
        if n%x==0:
            answer.append(x)
    answer.sort
    return answer

#Sum of even numbers
def solution(n):
    answer = 0
    for x in range(1,n+1):
        if x%2==0:
            answer=answer+x
    
    return answer
