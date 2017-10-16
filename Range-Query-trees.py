class Node:
	
	def __init__(self):

		self.parent=None
		self.left=None
		self.right=None
		self.start=-1
		self.end=-1
		self.val=0


class SegmentTree:

	def __init__(self,n):

		self.n=n-1
		self.root=None

	def design(self,s,e):

		
		x=Node()
		x.start=s
		x.end=e

		if e==self.n and s==0:
			self.root=x


		if s==e:
			return x

		else:
			m=int((s+e)/2)
			p=self.design(s,m)
			q=self.design(m+1,e)

			p.parent=x
			x.left=p

			q.parent=x
			x.right=q

		return x

	def sear(self,x,i,j):

		if x==None:
			return
		if x.start==i and x.end==j:
			return x

		else:
			p=self.sear(x.left,i,j)
			q=self.sear(x.right,i,j)
			if p!=None:
				return p
			if q!=None:
				return q
				

	def insert(self,a):

		n=len(a)

		for i in range(0,n):

			t=self.sear(self.root,i,i)
			t.val=a[i]

	def summing(self):

		for i in range(0,self.n+1):
			for j in range(i+1,self.n+1):

				for p in range(j-1,-1,-1):
					t=self.sear(self.root,p,j)
					if t!=None:
						t.val=t.right.val+t.left.val

				t=self.sear(self.root,i,j)

				if t!=None:
					t.val=t.right.val+t.left.val

				k=self.n-j
				t=self.sear(self.root,k,self.n)

				if t!=None:
					t.val=t.right.val+t.left.val

	def traversal(self,x):

		if x==None:
			return

		else:
			print(x.val)
			self.traversal(x.left)
			self.traversal(x.right)

	def intraversal(self,x):

		if x==None:
			return
		else:
			self.intraversal(x.left)
			print(x.val)
			self.intraversal(x.right)

	def rangesum(self,x,s,e):

		if s==x.start and e==x.end:

			return x.val

		elif (x.start<s and e<=x.end) or (s>=x.start and e<x.end) :

			p=0
			q=0

			if x.left!=None:
				if x.left.end>=s:
					if e<x.left.end:
						q=self.rangesum(x.left,s,e)
					else:
						q=self.rangesum(x.left,s,x.left.end)
			if x.right!=None:
				if x.right.start<=e:
					if s>x.right.start:
						p=self.rangesum(x.right,s,e)
					else:
						p=self.rangesum(x.right,x.right.start,e)
			
			return p+q

		elif x.start<s<x.end or x.start<e<x.end:

			p=0
			q=0

			if x.left!=None:
				if x.left.end>=s:
					q=self.rangesum(x.left,s,x.left.end)
			if x.right!=None:
				if x.right.start<=e:
					p=self.rangesum(x.right,x.right.start,e)
			

			return p+q

		else:

			return 0

	def update(self,i,n):

		t=self.sear(self.root,i,i)
		k=n-t.val
		self.add(self.root,t.start,t.end,k)

	def add(self,x,s,e,k):

		if s==x.start and e==x.end:

			x.val=x.val+k

		elif (x.start<s and e<=x.end) or (s>=x.start and e<x.end) :


			if x.left!=None:
				if x.left.end>=s:
					if e<x.left.end:
						x.val=x.val+k
						self.add(x.left,s,e,k)
					else:
						x.val=x.val+k
						self.add(x.left,s,x.left.end,k)
			if x.right!=None:
				if x.right.start<=e:
					if s>x.right.start:
						x.val=x.val+k
						self.add(x.right,s,e,k)
					else:
						x.val=x.val+k
						self.add(x.right,x.right.start,e,k)

		elif x.start<s<x.end or x.start<e<x.end:

			if x.left!=None:
				if x.left.end>=s:
					if e<x.left.end:
						x.val=x.val+k
						self.add(x.left,s,e,k)
					else:
						x.val=x.val+k
						self.add(x.left,s,x.left.end,k)
			if x.right!=None:
				if x.right.start<=e:
					if s>x.right.start:
						x.val=x.val+k
						self.add(x.right,s,e,k)
					else:
						x.val=x.val+k
						self.add(x.right,x.right.start,e,k)


def main():

	A=[5,2,1,3,4,6,7,9,8,3]
	s=SegmentTree(10)
	s.design(0,9)
	s.insert(A)
	s.summing()
	print('pre-traversal:')
	s.traversal(s.root)
	print('in-traversal:')
	s.intraversal(s.root)
	print('Sum of range',s.rangesum(s.root,3,8))
	s.update(3,6)
	print('after updating:')
	print('Sum of range',s.rangesum(s.root,3,8))



if __name__ == '__main__':
	main()
