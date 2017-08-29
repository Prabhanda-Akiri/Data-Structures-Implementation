def check(a):
    if a == '+' :
        return False

    if a == '-' :
        return False
    if a == '*' :
        return False
    if a == '/' :
        return False
    if a == '%' :
        return False
    else :
        return True

def calc(x,y,c):
    a=int(x)
    b=int(y)
    if c=='+' :
        return b + a
    elif c=='-' :
        return b - a
    elif c=='/' :
        return b / a
    elif c=='*' :
        return b * a
    else :
        return b % a




def main() :


    s='4 5 * 3 2 1 + / -'
    l=[]
    x=s.split()

    for i in range(len(x)):
        if check(x[i]):
            l.append(x[i])

        else :
            
            c=x[i]
            a=l.pop(-1)
            b=l.pop(-1)
            d=calc(a,b,c)
            
            l.append(d)
    
    r=l.pop(-1)
    print(r)

if __name__ == '__main__':
    main()

