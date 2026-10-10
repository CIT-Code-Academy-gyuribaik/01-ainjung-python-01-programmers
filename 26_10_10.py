짝수 홀수 개수

def solution(num_list):
    w=0
    q=0
    for x in num_list:
        if x%2==0:
            w=w+1
        else:
            q=q+1
    answer= [w,q]
    return answer

문자 반복 출력하기

def solution(my_string, n):
    answer=""
    for x in my_string:
        answer=answer+x*n
    return answer
