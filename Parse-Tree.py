class TreeNode:

	def __init__(self):

		self.parent=None
		self.left=None
		self.right=None
		self.value=0

class Node:

	def __init__(self):

		self.next=None

class ParseTree:

	def __init__(self):

		self.root=Node()
		self.current=None

	def insert(self,x):

		
			temp=TreeNode()
			
			if self.current==None:
				self.current=temp
				self.root.next=temp

			if x=='(':
				t=TreeNode()
				self.current.left=t
				t.parent=self.current
				self.current=t

			elif x=='+' or x=='-' or x=='/' or x=='*':
				self.current.value=x

				t=TreeNode()
				self.current.right=t
				t.parent=self.current
				self.current=t

			elif isnum(x):
				self.current.value=x
				self.current=self.current.parent

	def postfix(self,x):

		if x==None:
			return
		else:
			
			self.postfix(x.left)
			self.postfix(x.right)
			print(x.value)

	def prefix(self,x):

		if x==None:
			return
		else:
			print(x.value)
			self.prefix(x.left)
			self.prefix(x.right)

	def evaltree(self,x,s):
			if x==None:
				return
			else:
			
				self.evaltree(x.left,s)
				self.evaltree(x.right,s)
				s.append(x.value)
				s.append(" ")
			return s
		


def main():

	p=ParseTree()
	e=input('enter the expression:')
	for i in range(len(e)):

		p.insert(e[i])
	print('Post-order:')
	p.postfix(p.root.next)

	print('Pre-Order:')
	p.prefix(p.root.next)
	post="".join(p.evaltree(p.root.next,[]))
	print('Post-fix expression:',post)
	print('Answer:',eval(post))
	


def isnum(x):

	if ord(x)>=48 and ord(x)<=57:
		return True
	return False

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




def eval(p):


    s=p
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
    return r



if __name__ == '__main__':
	main()

