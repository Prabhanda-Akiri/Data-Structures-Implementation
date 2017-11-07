class GraphNode:

	def __init__(self):

		self.val=-1
		self.color=None
		self.start='inf'
		self.end='inf'
		self.pred=None
		self.list=[]

class Edges:

	def __init__(self):

		self.s=-1
		self.e=-1
		self.type='edge'


class DFS:

	def __init__(self,n,s,e):


		self.Q=[]
		self.source=None
		self.time=-1
		self.p=[None for i in range(n)]
		self.E=[None for i in range(e)]

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

		for i in range(len(self.p)):

			#print(L[i])
			for j in range(0,len(L[i])):

				self.p[i].list.append(self.p[L[i][j]])

			print('Vertex ',i,end=':	')

			for k in range(len(self.p[i].list)):
				print(self.p[i].list[k].val,end=' ')
			print(" ")

	def dfs(self):

		self.applydfs(self.source)

		print('\nTime Stamps for the vertices after the DFS:')

		for i in range(len(self.p)):

			print('Vertex:',i,'	start=',self.p[i].start,'	end=',self.p[i].end)

	def applydfs(self,u):

		self.time=self.time+1
		u.start=self.time

		u.color='grey'

		for i in range(len(u.list)):

			if u.list[i].color=='white':

				self.applydfs(u.list[i])
				u.list[i].pred=u

		u.color='black'

		self.time=self.time+1
		u.end=self.time

		return

	def EdgeTypes(self,G):

		for i in range(len(G)):

			u=G[i][0]
			v=G[i][1]

			A=Edges()
			self.E[i]=A

			A.s=u
			A.e=v

			if self.p[u].start>self.p[v].start and self.p[u].end>self.p[v].end:

				A.type='Cross Edge'

			elif self.p[u].start<self.p[v].start and self.p[v].end<self.p[u].end:

				A.type='Forward Edge'

				if self.p[v].pred==self.p[u]:
					A.type='Tree Edge'

			elif self.p[u].start>self.p[v].start and self.p[v].end>self.p[u].end:

				A.type='Back Edge'


		for i in range(len(self.E)):

			#print('\nEdge:',i)

			print('\nSource:',self.E[i].s,'\nDestination:',self.E[i].e,'\nType:	',self.E[i].type)

def main():

	n=8
	e=13

	G=[[0,1],[0,2],[1,4],[5,1],[4,5],[5,6],[4,6],[4,7],[7,6],[3,7],[3,0],[2,3],[0,5]]

	V=adjacencylist(G,n)

	D=DFS(n,0,e)
	D.build(V)
	D.dfs()
	D.EdgeTypes(G)


def adjacencylist(graph,n):

	l=[[] for j in range(n)]


	for i in range(len(graph)):

		l[graph[i][0]].append(graph[i][1])

		#print(l)
	return l


if __name__ == '__main__':
	main()
