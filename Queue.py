class ListNode :

	def __init__(self) :

		self.value=0
		self.next=None

class Queue :

	def __init__(self) :

		self.head=None
		self.tail=None

	def enqueue(self,x) :

		temp=ListNode()
		temp.value=x

		if self.isEmpty() :
			self.tail=temp
			self.head=temp
			
		else :

			self.tail.next=temp
			self.tail=temp


	def dequeue(self) :

		if self.isEmpty() :
			print("queue is empty element can't be dequeued")

		else :

			self.head=self.head.next

	def front(self) :

		print(self.head.value)

	def isEmpty(self):

		if self.head :

			return False

		else :
			return True

	def size(self) :

		temp=ListNode()
		temp=self.head
		count=0

		while temp :

			count=count+1
			temp=temp.next

		print(count)

	def printq(self) :

		temp=ListNode()
		temp=self.head

		while temp :

			print(temp.value)
			temp=temp.next


def main() :

	Q=Queue()

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
	Q.size()

	print("Q is empty?",Q.isEmpty())


if __name__ == '__main__':
	main()
