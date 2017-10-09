import time

class TreeNode:

    def __init__(self):
        self.parent=None
        self.left=None
        self.right=None
        self.value=0
        self.s='a'
class Node:
    
    def __init__(self):
        self.next=None

class OrderedDict:

    def __init__(self):
        self.root=Node()

    def insert(self,x,s):

        t=TreeNode()
        t.value=x
        t.s=s
        temp=TreeNode()
        p=0
        if self.root.next==None:

            self.root.next=t
        else:

            temp=self.root.next
            te=self.root.next
            
            while temp!=None:
                if t.value>temp.value:
                    te=temp
                    temp=temp.right
                    p=1
                    
                elif t.value<temp.value:
                    te=temp
                    temp=temp.left
                    p=2
                
            t.parent=te
            if p==1:
                te.right=t
                
            elif p==2:
                te.left=t

        return
    def search(self,x):

        temp=TreeNode()
        temp=self.root.next
        while temp!=None:

            if x>temp.value:
                temp=temp.right
            elif x<temp.value:
                temp=temp.left
            elif x==temp.value:
                return temp

    def minimum(self,x):

        temp=TreeNode()
        temp=x
        while temp.left!=None:

            temp=temp.left

        return temp
    def maximum(self,x):

        temp=TreeNode()
        temp=x
        while temp.right!=None:

            temp=temp.right

        return temp

    def successor(self,x):

        if x.right!=None:

            return self.minimum(x.right)
        y=x.parent

        while x!=y.left and y!=None:

            x=y
            y=y.parent

        return y

    def predecessor(self,x):

        if x.left!=None:

            return self.maximum(x.left)
        y=x.parent

        while x!=y.right and y!=None:

            x=y
            y=y.parent
        return y

    def delete(self,x):

        if x.right==None and x.left==None:

            if x.parent.right==x:

                x.parent.right=None
            else:
                x.parent.left=None

        elif x.right==None or x.left==None:

            if x.parent.right==x:

                if x.right==None:
                    x.parent.right=x.left
                else:
                    x.parent.right=x.right

            if x.parent.left==x:

                if x.right==None:
                    x.parent.left=x.left
                else:
                    x.parent.left=x.right
        else:

            y=self.predecessor(x)
            x.value=y.value
            x.s=y.s
            y.parent.right=y.left


        return

    def traversal(self,x):

        if x==None:

            return
        else:
            print(x.s)
            print(x.value)
            self.traversal(x.left)
            self.traversal(x.right)

    def val(self,x):

        print(x.s)
        print(x.value)

class BST:

    def __init__(self):

        self.D=OrderedDict()
    def ins(self,s):
        x=key(s)
        self.D.insert(x,s)
    def dele(self,s):
        x=key(s)
        self.D.delete(self.D.search(x))
    def sear(self,s):
        x=key(s)
        self.D.val(self.D.search(x))
    def min(self):
        self.D.val(self.D.minimum(self.D.root.next))
    def max(self):
        self.D.val(self.D.maximum(self.D.root.next))

    def printlist(self):
        self.D.traversal(self.D.root.next)


def main():

    b=BST()
    b.ins('juggler')
    b.ins('cartoon')
    b.ins('basket')
    b.ins('zoo')
    b.ins('ink')
    b.ins('honest')
    b.ins('game')
    print('after inserting')
    b.printlist()
    print('after deleting "basket"')
    b.dele('basket')
    b.printlist()
    print('minimum is')
    b.min()
    print('maximum is')
    b.max()



def key(s):
    k=0
    for i in range(len(s)):

        k=k+ord(s[i])
    return k

start_time = time.time()
main()
print("--- %s seconds --- " % (time.time() - start_time))
