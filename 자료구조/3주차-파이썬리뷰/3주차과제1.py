#교재46p_1.14

def asterisk(i):
    if i > 1:
        asterisk(i/2)
        asterisk(i/2)
    print("*", end='')


asterisk(9)
