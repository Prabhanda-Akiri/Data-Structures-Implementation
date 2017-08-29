class ListNode:
    def __init__(self) :
        self.value=0
        self.next=None

class Stack:

    def __init__(self) :
        self.root=None

    def push(self,x) :
        temp=ListNode()
        temp.value=x
        temp.next=self.root
        self.root=temp

    def pop(self) :
        c=self.root.value
        self.root=self.root.next
        return c


def main():

    s='4 5 * 3 2 1 + / -'
    l=Stack()
    x=s.split(" ")

    for i in range (0,len(x)) :
        

        if check(x[i]) :
            l.push(x[i])

        else :
            c=x[i]
            a=l.pop()
            b=l.pop()
            d=calc(a,b,c)
            l.push(d)

    r=l.pop()

    print(r)



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


if __name__ == '__main__':
    main()
