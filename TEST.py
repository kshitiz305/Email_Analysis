# li = [1,2,2,4]
#
# # print(list(set(li)))
#
#
# res = []
# for i in li:
#     if i not in res:
#         res.append(i)
# print(res)

inputstr = "}}"

openingbrace = ["[","{","("]
closingbrace = ["]","}",")"]


stack = []

def equal_brace():
    # flag = True
    if len(inputstr) % 2 != 0:
        return "Not equal"
    for i in inputstr:
        if i in openingbrace:
            stack.append(i)
        elif len(stack) > 0:
            ele2 = stack.pop()
            if openingbrace.index(ele2) == closingbrace.index(i):
                continue

            else:
                return "Not Equal"
    if len(stack) != 0:
        return "Not Equal"

    return "Equal"

print(equal_brace())



def solution(A, K, L):
    # write your code in Python 3.8.10
    if len(A) < K + L :
      return -1
    else:
      start = sum1 = sum2 =  0
      while start+K < len(A):
        su = sum(A[start:start+K])
        if su > sum1:
            sum1 = su
            pos1= start
            pos2 = start+K
        start+=1
    start = 0
    while len(A[start:pos1]) <= L and start<=pos1-L:
        su = sum(A[start:start+L])
        if su > sum2:
            sum2 = su
        start +=1
    start = 0
    while len(A[pos2:]) >= L and start<=len(A[pos2:])-2:
        su = sum(A[pos2+start:pos2+ L+start])
        if su > sum2:
            sum2 = su
        start += 1

    return sum1 + sum2


print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))


