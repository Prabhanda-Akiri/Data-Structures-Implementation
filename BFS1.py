def adjacencylist(graph,n):

	l=[[0 for i in range(1)] for j in range(n-1)]
	#print(l)

	for i in range(n):

		l[graph[i][0]].append(graph[i][1])
		l[graph[i][1]].append(graph[i][0])

	print('\nThe adjacency List is:\n')

	for i in range(n-1):

		print('Vertex ',i,': '),
		for j in range(1,len(l[i])):

			print(l[i][j]),

		print('')



def edgematrix(graph,n):

	m=[[0 for i in range(n-1)] for j in range(n-1)]

	for i in range(n):

		m[graph[i][0]][graph[i][1]]=1
		m[graph[i][1]][graph[i][0]]=1

	#print(m)

	print('\nAdjacency matrix:\n')
	for i in range(n-1):
		for j in range(n-1):
			print(m[i][j]),
		print(' ')


def main():

	n=6
	"""graph=[[0 for i in range(2)] for i in range(n)]

	for i in range(n):
		for j in range(2):

			graph[i][j]=int(input())

	"""

	graph=[[0,1],[0,2],[1,2],[1,3],[1,4],[2,3]]

	print('Edges:\n')
	for i in range(n):
		for j in range(2):
			print(graph[i][j]),
		print('')

	edgematrix(graph,n)
	adjacencylist(graph,n)



if __name__ == '__main__':
	main()
