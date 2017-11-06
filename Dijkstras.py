class GraphNode:

	def __init__(self):

		self.val=None
		self.dist=999
		self.adj=[]
		self.list=[]
		self.weight=[]

class Dijkstras:

	def __init__(self,n,s):

		self.source=None

		self.p=[None for i in range(n)]

		for i in range(n):

			u=GraphNode()
			self.p[i]=u

			u.val=i

			if i==s:

				self.source=u


	def build(self,L):

		for i in range(len(L)):
			for j in range(1,len(L[i])):

				k=int(i/2)

				if i%2==0:					

					for o in range(len(self.p)):
						if self.p[o].val==L[i][j]:
							d=self.p[o]
							break
					self.p[k].list.append(d)

				else:

					self.p[k].weight.append(L[i][j])


		"""for i in range(len(self.p)):

			print('\nVetex:',i)
			print('Adjacent vertices:',self.p[i].list)
			print('Weight of edges:',self.p[i].weight)"""


	def shortestpath(self):

		self.source.dist=0
		q=PriorityQueue()

		for i in range(len(self.p)):

			q.ins(self.p[i])

		q.build()


		while q.Qu.last!=0:

			#q.printlist()
			v=q.exmin()

			print(v.val)

			for i in range(len(v.list)):

				if v.list[i].dist+v.weight[i]<v.dist:

					k=v.dist
					v.list[i].dist=v.list[i].dist+v.weight[i]

					q.up(v.dist,k)

		for i in range(len(self.p)):

			print(self.p[i].dist)

def main():

	n=5

	graph=[[0,1,10],[0,3,5],[3,1,3],[3,2,9],[3,4,2],[4,2,4],[4,0,7],[1,3,2],[1,2,1],[2,4,6]]

	List=adjacencylist(graph,n)

	d=Dijkstras(n,0)
	d.build(List)
	d.shortestpath()




def adjacencylist(G,n):

	l=[[0 for i in range(1)]for i in range(2*n)]

	for i in range(len(G)):

		l[2*(G[i][0])].append(G[i][1])

		l[2*(G[i][0])+1].append(G[i][2])

	print(l)

	return l



class PriorityQueue:

	def __init__(self):

		self.Qu=Heap()

	def ins(self,a):

		self.Qu.insert(a)

	def build(self):

		self.Qu.buildheap()

	def min(self):
		return self.Qu.minimum()

	def printlist(self):
		
		self.Qu.list()

	def exmin(self):
		return self.Qu.extractmin()

	def up(self,v,k):

		self.Qu.update(v,k)

	def printlist(self):

		self.Qu.list()


class Heap:

	def __init__(self):

		self.a=['a']
		self.last=0

	def insert(self,x):

		self.a.append(x)
		self.last=self.last+1


	def heapifydown(self):

		
		for i in range(1,self.last+1):

			p=2*i+1
			q=2*i

			if p<=self.last:

				if self.a[p].dist<self.a[q].dist:
					if self.a[p].dist<self.a[i].dist:
						temp=self.a[p]
						self.a[p]=self.a[i]
						self.a[i]=temp

				elif self.a[q].dist<self.a[p].dist:
					if self.a[q].dist<self.a[i].dist:
						temp=self.a[q]
						self.a[q]=self.a[i]
						self.a[i]=temp
			elif q<=self.last:

				if self.a[q].dist<self.a[i].dist:
						temp=self.a[q]
						self.a[q]=self.a[i]
						self.a[i]=temp

	def heapifyup(self):

		for i in range(self.last,1,-1):

			if i%2==0:
				p=i/2
			else:
				p=(i-1)/2
			k=int(p)

			if self.a[k].dist>self.a[i].dist:

				temp=self.a[k]
				self.a[k]=self.a[i]
				self.a[i]=temp
		
	def minimum(self):

		return self.a[1]

	def extractmin(self):

		m=self.a[1]
		self.a[1]=self.a[self.last]
		self.last=self.last-1
		self.heapifyup()
		self.heapifydown()
		return m


	def buildheap(self):

		self.heapifyup()
		self.heapifydown()

	def update(self,v,k):

		for i in range(len(self.a)):

			if self.a[i].dist==k:

				self.a[i].dist=v
				self.buildheap()
				break
		return



	def list(self):

		print(self.a[1:self.last+1])


if __name__ == '__main__':
	main()
