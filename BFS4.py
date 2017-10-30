class GraphNode:

	def __init__(self):

		self.val=-1
		self.color=None
		self.distance='inf'
		self.pred=None
		self.list=[]

class BFS:

	def __init__(self,n,s):


		self.Q=[]
		self.source=None

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

		for i in range(len(self.p)-1):

			#print(L[i])
			for j in range(1,len(L[i])):

				self.p[i].list.append(self.p[L[i][j]])

			print('Vertex ',i,end=':	')

			for k in range(len(self.p[i].list)):
				print(self.p[i].list[k].val,end=' ')
			print(" ")


	def apply(self):


		while(len(self.Q)!=0):

			u=self.Q.pop(0)
			n=len(u.list)

			for i in range(0,n):

				if u.list[i].color=='white':

					u.list[i].distance=u.distance+1
					u.list[i].color='grey'
					u.list[i].pred=u
					print('\nVertex:	',u.list[i].val)
					print('dist:',u.list[i].distance)
					self.Q.append(u.list[i])

				else:

					if u.list[i].distance==u.distance:

						k=self.sear(u.list[i],u)

						u.list[i].list.pop(k)
						u.list.pop(i)
						i=i-1
						n=n-1


			u.color='black'


		for k in range(len(self.p[i].list)):
			print(self.p[i].list[k].val,end=' ')
		print(" ")

		return


	def sear(self,x,y):

		for i in range(len(x.list)):

			if x.list[i]==y:

				return i

def main():

	n=8

	graph=[[1,2],[0,1],[0,3],[3,4],[4,6],[3,6],[4,5],[6,5],[6,7],[7,5]]
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
