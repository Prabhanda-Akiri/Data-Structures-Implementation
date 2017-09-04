class queuelist :

	def __init__(self) :

		self.q=[]

	def enqueue(self,x) :

		self.q.append(x)

	def dequeue(self) :

		if self.isEmpty() :

			print('the queue is empty')

		else :

		    self.q.pop(0)

	def front(self) :

		print(self.q[0])

	def isEmpty(self) :

		if self.size()==0 :
			return True

		else :
			return False

	def size(self) :

		return len(self.q)

	def printq(self) :

		for i in range(0,len(self.q)) :

			print(self.q[i])



def main() :


	Q=queuelist()

	Q.enqueue(5)
	print("Now the queue is")
	Q.printq()

	Q.enqueue(4)
	print("Now the queue is")
	Q.printq()

	Q.enqueue(9)
	print("Now the queue is")
	Q.printq()

	Q.enqueue(13)
	print("Now the queue is")
	Q.printq()

	Q.dequeue()
	print("Now the queue is")
	Q.printq()

	print("the element at the front is")
	Q.front()

	Q.enqueue(18)
	Q.enqueue(6)
	print("Now the queue is")
	Q.printq()

	print("size of the queue is")
	print(Q.size())

	print("Q is empty?",Q.isEmpty())


if __name__ == '__main__':
	main()






