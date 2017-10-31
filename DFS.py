class GraphNode:

	def __init__(self):

		self.val=-1
		self.color=None
		self.start='inf'
		self.end='inf'
		self.pred=None
		self.list=[]

class DFS:

	def __init__(self,n,s):


		self.Q=[]
		self.source=None
		self.time=-1
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
				self.time=self.time+1
				r.start=self.time
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

	def dfs(self):

		self.applydfs(self.source)

		for i in range(len(self.p)):

			print('Vertex:',i,'	start=',self.p[i].start,'	end=',self.p[i].end)

	def applydfs(self,u):

		self.time=self.time+1
		u.start=self.time

		u.color='grey'

		for i in range(len(u.list)):

			if u.list[i].color=='white':

				self.applydfs(u.list[i])
				u.list[i].predecessor=u

		u.color='black'

		self.time=self.time+1
		u.end=self.time

		return




def main():

	n=8

	graph=[[1,2],[0,1],[0,3],[3,4],[4,6],[3,6],[4,5],[6,5],[6,7],[7,5]]
	#print(len(graph))

	List=adjacencylist(graph,n)

	s=0

	b=DFS(n,s)
	b.build(List)
	b.dfs()


def adjacencylist(graph,n):

	l=[[0 for i in range(1)] for j in range(n)]


	for i in range(len(graph)):

		l[graph[i][0]].append(graph[i][1])
		l[graph[i][1]].append(graph[i][0])


		#print(l)
	return l




if __name__ == '__main__':
	main()
