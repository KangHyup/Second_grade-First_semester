# 중위표기를 후위표기로 바꿔주는 함수

from stackClass import Stack

#연산자 우선순위
def precedence(op):
    if op =='(' or op ==')': return 0
    elif op =='+' or op =='-': return 1
    elif op =='*' or op =='/': return 2
    else : return -1

def Infix2Postfix(expr):
    s=Stack()
    output=[]
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(': break;    #맨밑에 있는 '('가 나올때 까지 저장했던 연산자를 출력
                else:
                    output.append(op)

        elif term in "+-*/":            #연산자를 만나면 우선순위가 높거나 같은 연산자를 스택에서 output으로 모두 옮김
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break

            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty():
            output.append(s.pop())
    
    return output



print(Infix2Postfix("a*(b+(c*d-e)/f))+g"))