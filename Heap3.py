class Node:

	def __init__(self,i):

		self.parent=None
		self.left=None
		self.right=None
		self.index=i
		self.val=0

class Bt:

	def __init__(self):

		self.no=7
		self.n=['a']
		for i in range(1,8):

			self.n.append(Node(i))

		self.root=self.n[1]

	def initialisation(self):

		self.n[1].val=23
		self.n[2].val=20
		self.n[3].val=18
		self.n[4].val=12
		self.n[5].val=11
		self.n[6].val=16
		self.n[7].val=2

		for i in range(1,4):

			self.n[i].left=self.n[2*i]
			self.n[2*i].parent=self.n[i]
			if 2*i+1<=7:
				self.n[i].right=self.n[2*i+1]
				self.n[2*i+1].parent=self.n[i]

	def sear(self,x,n):

		if x!=None:
			if x.index==n:

				return x

			else:

				p=self.sear(x.right,n)
				q=self.sear(x.left,n)

				if p!=None:
					return p
				if q!=None:

					return q

		

	def traversal(self,x):

		if x==None:
			return

		else:
			print(x.val)
			self.traversal(x.left)
			self.traversal(x.right)


	def isBinaryHeap(self,n):

		p=0
		for i in range(0,n):

			t=self.sear(self.root,i+1)
			print('searched element:',t.val)
			if (2*(i+1))<=n:
				if t.left==None:
					p=1
					break

			if 2*(i+1)+1<=n:
				if t.right==None:
				
					p=1
					break

				if t.right.val>t.val or t.left.val>t.val:
					p=1
					break

		if p==1:

			return False
		return True

def main():

	b=Bt()
	b.initialisation()
	print('Traversal of the binary tree:')
	b.traversal(b.root)
	print(b.isBinaryHeap(7))


if __name__ == '__main__':
	main()

