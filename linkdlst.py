# singly-linked-list-operations using python

class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()

    def insert(self,x,p):
        """Insert element x in the position after p"""
        self.temp=ListNode()
        self.temp.value=x
        
        self.temp.next=p.next
        p.next=self.temp

    def delete(self,p):
        """Delete the node following node p in the linked list."""
        p.next=p.next.next

    def printlist(self):
        """ Print all the elements of a list in a row."""
        self.temp=ListNode()
        self.temp=self.head.next

        while self.temp != None :
            
            print (self.temp.value)
            self.temp=self.temp.next
        

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        self.temp=ListNode()
        self.temp=self.head
        self.count=0
        while 1 :
            if self.count == i :
                self.insert(x,self.temp)
                break
            else :
                self.temp=self.temp.next
                self.count=self.count+1


    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        self.temp=ListNode()
        self.temp=self.head
        while 1 :
            self.temp=self.temp.next
            if self.temp.value == x :
                return self.temp


    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        self.temp=ListNode()
        self.temp=self.head.next
        
        self.count=0
        while self.temp!=None:
                self.count=self.count+1
                self.temp=self.temp.next
            
        return self.count

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.len() == 0 :
            return True
        else :
            return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self):
        self.value=0
        self.next=None

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ')
    L.printlist()
    L.insert(12,L.head.next)
    print('List is: ')
    L.printlist()
    L.insert(2,L.head)
    print('List is: ')
    L.printlist()
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ')
    L.printlist()
    L.delete(L.head.next)
    print('List is: ')
    L.printlist()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ')
    L.printlist()

if __name__ == '__main__':
    main()

