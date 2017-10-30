class GraphNode:

	def __init__(self):

		self.val=-1
		self.color=None
		self.pred=None
		self.list=[]

class BFS:

	def __init__(self,n,s):


		self.r=[None for i in range(n)]
		self.Q=[]
		self.source=None
		self.t=0
		self.p=[None for i in range(n)]

		for i in range(n):

			r=GraphNode()
			r.val=i
			self.p[i]=r

			if i!=s:

				r.color='white'
			else:
				self.source=r
				r.color='grey'
				r.distance=0
				self.Q.append(r)

	def build(self,L):

		for i in range(len(self.p)):

			#print(L[i])
			for j in range(1,len(L[i])):

				self.p[i].list.append(self.p[L[i][j]])

			print('Vertex ',i,end=':	')

			for k in range(len(self.p[i].list)):
				print(self.p[i].list[k].val,end=' ')
			print(" ")


	def apply(self):


		for i in range(len(self.p)):

			if self.r[i]==None:

				self.t=self.t+1
				self.r[i]=self.t
				self.Q.append(self.p[i])

				while(len(self.Q)!=0):

					u=self.Q.pop(0)

					for i in range(0,len(u.list)):

						if u.list[i].color=='white':

							u.list[i].color='grey'
							u.list[i].pred=u

							self.r[u.list[i].val]=self.t
							print('\nVertex:	',u.list[i].val)
							self.Q.append(u.list[i])

						u.color='black'

		print('\nThe component Array is:')
		print(self.r)


		print('\nThere are ',self.t,' connected components in the graph given')
		return



def main():

	n=11

	graph=[[0,4],[0,5],[4,5],[1,6],[2,3],[2,7],[2,10],[3,8],[8,10],[7,8]]
	#print(len(graph))

	List=adjacencylist(graph,n)

	s=0

	b=BFS(n,s)
	b.build(List)
	b.apply()


def adjacencylist(graph,n):

	l=[[0 for i in range(1)] for j in range(n)]


	for i in range(len(graph)):

		l[graph[i][0]].append(graph[i][1])
		l[graph[i][1]].append(graph[i][0])


		#print(l)
	return l




if __name__ == '__main__':
	main()
