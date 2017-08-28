class ListNode :

	def __init__(self) :
		self.value=0
		self.next=None

class Stack :

	def __init__(self) :
		self.root=None

	def isEmpty(self) :
		if self.root :
			return False
		else :
			return True

	def push(self,x) :
		self.temp=ListNode()
		self.temp.value=x
		self.temp.next=self.root
		self.root=self.temp

	def pop(self) :
		if self.size() :
			self.root=self.root.next

		else :
			print ('the stack is empty')

	def top(self):
		if self.size() :
			return self.root.value

	def size(self) :
		self.count=0
		self.temp=ListNode()
		self.temp=self.root
		while self.temp :
			self.count=self.count + 1
			self.temp=self.temp.next

		return self.count

	def printstack(self) :
		self.temp=ListNode()
		self.temp=self.root
		while self.temp != None :
			print (self.temp.value)
			self.temp=self.temp.next




def main() :

	s=Stack()
	s.push(5)
	s.push(4)
	print ('now the list is')
	s.printstack()
	s.push(6)
	s.push(9)
	print ('now the list is')
	s.printstack()
	s.pop()
	print ('now the list is')
	s.printstack()
	s.pop()
	print ('now the list is')
	s.printstack()
	print('size of the stack is')
	print(s.size())
	print('element at the top is')
	print(s.top())
	print('is stack empty?',s.isEmpty())
	print ('now the list is')
	s.printstack()	

if __name__ == '__main__':
	main()

