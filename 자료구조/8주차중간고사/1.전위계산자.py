
from stackClass import Stack

def evalPrefix(expr):
    s=Stack()

    ary = []
    for i in expr: s.push(i)
    for i in expr: ary.append(s.pop())
    print(ary)

    for token in ary:
            if token in "+-*/":
                val2 = s.pop()
                val1 = s.pop()
                if (token == '+'): s.push(val1 + val2)
                elif (token == '-'): s.push(val2 - val1)
                elif (token == '*'): s.push(val1 * val2)
                elif (token == '/'): s.push(val2 / val1)
            else: 
                s.push(float(token))

    return s.pop()

ary = list("+/*4+3-211*23")
print(evalPrefix(ary))