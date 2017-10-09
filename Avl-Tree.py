class AvlNode:
	def __init__(self):

		self.parent=None
		self.left=None
		self.right=None
		self.s=0
		self.value=0
		self.height=0
class Node:
	
	def __init__(self):
		self.next=None

class AvlTree:

	def __init__(self):

		self.root=None

	def insert(self,k,s):

		t=AvlNode()
		t.value=k
		t.s=s
		t.height=1

		if self.root==None:
			self.root=t
		else:
			temp=AvlNode()
			temp=self.root
			te=AvlNode()
			te=self.root
			p=0
			
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
			c=AvlNode()
			c=t.parent

			if p==1:
				te.right=t
				
			elif p==2:
				te.left=t

			while c!=None:
					if c.left==None:
						if c.right.height<2:
							c.height=c.right.height+1
						else:
							c.height=c.right.height+1
							n=c
							break
					elif c.right==None:

						if c.left.height<2:
							c.height=c.left.height+1
						else:
							c.height=c.left.height+1
							n=c
							break
					
					elif c.left.height-c.right.height<2 and c.left.height-c.right.height>-2:
						if c.left.height>c.right.height:
							c.height=c.left.height+1
						else:
							c.height=c.right.height+1
					else:
						if c.left.height>c.right.height:
							c.height=c.left.height+1
							n=c
							break
						else:
							c.height=c.right.height+1
							n=c 
							break

					c=c.parent
			
			
			if t.parent.parent!=None and t.parent.parent.parent!=None:
				x=t
				y=x.parent
				z=y.parent
				while z.parent!=None:

					if z==n:
						break
					else:
						z=z.parent
						y=y.parent
						x=x.parent
				k=0
				if z.left==None:
					if z.right.height>1:
						k=2
				if z.right==None:
					if z.left.height>1:
						k=2


				if k==2 or z.right.height-z.left.height>1 or z.right.height-z.left.height<-1:
					if z.left==y and y.left==x:
						if y.right!=None:
							temp=y.right
							temp.parent=z
						y.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=y
							else:
								z.parent.left=y
						y.right=z
						z.left=temp
						z.parent=y
						z.height=z.height-2
						if self.root==z:
							self.root=y
					

					elif z.right==y and y.right==x:
						if y.left!=None:
							temp=y.left
							temp.parent=z
						y.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=y
							else:
								z.parent.left=y
						y.left=z
						z.right=temp
						z.parent=y
						z.height=z.height-2
						if self.root==z:
							self.root=y
					
					elif z.left==y and y.right==x:
						temp1=x.left
						temp2=x.right
						x.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=x
							else:
								z.parent.left=x

						y.parent=x
						y.right=temp1
						if temp1!=None:
							temp1.parent=y
						x.left=y
						x.right=z
						z.parent=x
						z.left=temp2
						if temp2!=None:
							temp2.parent=z
						y.height=y.height-1
						x.height=x.height+1
						z.height=z.height-2
						if self.root==z:
							self.root=x



					elif z.right==y and y.left==x:
						temp1=x.left
						temp2=x.right
						x.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=x
							else:
								z.parent.left=x
						x.left=z
						z.parent=x
						x.right=y
						y.parent=x
						y.left=temp2
						if temp2!=None:
							temp2.parent=y
						z.right=temp1
						if temp1!=None:
							temp1.parent=z
						z.height=z.height-2
						x.height=x.height+1
						y.height=y.height-1
						if self.root==z:
							self.root=x


				
		return

	def delete(self,x):

		
		if x.right==None and x.left==None:
			t=x.parent
			if x.parent.right==x:

				x.parent.right=None
			else:
				x.parent.left=None

		elif x.right==None or x.left==None:
			t=x.parent
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
			t=y.parent
		c=t
		z=None

		while c!=None:
			if c.left==None:
				c.height=c.right.height+1
			elif c.right==None:
				c.height=c.left.height+1

			elif c.left.height-c.right.height<2 and c.left.height-c.right.height>-2:
				if c.left.height>c.right.height:
					c.height=c.left.height+1
				else:
					c.height=c.right.height+1

			else:
				c.height=c.height-1
				z=c
				break

			g=c
			c=c.parent
		if z!=None:

			if z.right==g:
				y=z.left
				if y.left.height>y.right.height:
					x=y.left
				else:
					x=y.right
			else:
				y=z.right
				if y.left.height>y.right.height:
					x=y.left
				else:
					x=y.right


			if z.left==y and y.left==x:
						if y.right!=None:
							temp=y.right
							temp.parent=z
						y.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=y
							else:
								z.parent.left=y
						y.right=z
						z.left=temp
						z.parent=y
						z.height=z.left.height+1
						y.height=z.height+1
						if self.root==z:
							self.root=y
					
			elif z.right==y and y.right==x:
						if y.left!=None:
							temp=y.left
							temp.parent=z
						y.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=y
							else:
								z.parent.left=y
						y.left=z
						z.right=temp
						z.parent=y
						z.height=z.right.height+1
						y.height=z.height+1
						if self.root==z:
							self.root=y
					
			elif z.left==y and y.right==x:
						temp1=x.left
						temp2=x.right
						x.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=x
							else:
								z.parent.left=x

						y.parent=x
						y.right=temp1
						if temp1!=None:
							temp1.parent=y
						x.left=y
						x.right=z
						z.parent=x
						z.left=temp2
						if temp2!=None:
							temp2.parent=z
						y.height=y.height-1
						x.height=x.height+1
						z.height=z.height-2
						if self.root==z:
							self.root=x



			elif z.right==y and y.left==x:
						temp1=x.left
						temp2=x.right
						x.parent=z.parent
						if z.parent!=None:
							if z.parent.right==z:
								z.parent.right=x
							else:
								z.parent.left=x
						x.left=z
						z.parent=x
						x.right=y
						y.parent=x
						y.left=temp2
						if temp2!=None:
							temp2.parent=y
						z.right=temp1
						if temp1!=None:
							temp1.parent=z
						z.height=z.height-2
						x.height=x.height+1
						y.height=y.height-1
						if self.root==z:
							self.root=x




	

	def search(self,x):

		temp=AvlNode()
		temp=self.root
		while temp!=None:

			if x>temp.value:
				temp=temp.right
			elif x<temp.value:
				temp=temp.left
			elif x==temp.value:
				return temp

	def minimum(self,x):

		temp=AvlNode()
		temp=x
		while temp.left!=None:

			temp=temp.left

		return temp
	def maximum(self,x):

		temp=AvlNode()
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

	def pretraversal(self,x):

		if x==None:

			return

		else:

			print(x.s)
			print(x.height)
			self.pretraversal(x.left)
			self.pretraversal(x.right)
	def val(self,x):

		print(x.s)
		print(x.value)


class BST:

	def __init__(self):

		self.D=AvlTree()
	def ins(self,s):
		x=key(s)
		self.D.insert(x,s)
	def printlist(self):
		self.D.pretraversal(self.D.root)
	def sear(self,s):
		x=key(s)
		self.D.val(self.D.search(x))
	def min(self):
		self.D.val(self.D.minimum(self.D.root))
	def max(self):
		self.D.val(self.D.maximum(self.D.root))
	def dele(self,s):
		x=key(s)
		self.D.delete(self.D.search(x))

def main():

	b=BST()
	b.ins('juggler')
	b.printlist()
	print('cartoon:')
	b.ins('cartoon')
	b.printlist()
	print('basket:')
	b.ins('basket')
	b.printlist()
	print('zoo:')
	b.ins('zoo')
	b.printlist()
	print('ink:')
	b.ins('ink')
	b.printlist()
	print('honest:')
	b.ins('honest')
	b.printlist()
	b.ins('game')
	print('after inserting:')
	b.printlist()
	print('minimum is')
	b.min()
	print('maximum is')
	b.max()
	print('after deleting "basket"')
	b.dele('basket')
	b.printlist()

def key(s):
	k=0
	for i in range(len(s)):

		k=k+ord(s[i])
	return k

if __name__ == '__main__':
	main()
