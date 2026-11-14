#elements with n intervals
def solution(num_list, n):
    answer = []
    for x in range(0,len(num_list),n):
        answer.append(num_list[x])
    return answer
#The first negative number
def solution(num_list):
    answer = 0
    for x in num_list:
        if x>=0:
            answer=answer+1
        else:
            return answer
    return -1
#Combine into larger size
def solution(a, b):
    answer1 = int(str(a)+str(b))
    answer2=int(str(b)+str(a))
    if answer1>answer2:
        return answer1
    else:
        return answer2
