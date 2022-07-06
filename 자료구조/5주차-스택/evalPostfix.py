# 후위표기를 연산하는 함수

from stackClass import Stack

def evalPostfix(expr):
    s=Stack()
    for token in expr:
            if token in "+-*/":
                val2 = s.pop()
                val1 = s.pop()
                if (token == '+'): s.push(val1 + val2)
                elif (token == '-'): s.push(val1 - val2)
                elif (token == '*'): s.push(val1 * val2)
                elif (token == '/'): s.push(val1 / val2)
            else: 
                s.push(float(token))

            print(s.top)

    return s.pop()

print(evalPostfix("32*112-3+4*/+"))