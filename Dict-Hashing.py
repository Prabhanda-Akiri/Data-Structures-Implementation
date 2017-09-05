class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode('a')

    def insert(self,x,s):
        """Insert element x in the position after p"""
        self.temp=ListNode(s)
        self.temp.value=x
        
        self.temp.next=self.head.next
        self.head.next=self.temp

    def delete(self,p):
        """Delete the node following node p in the linked list."""
        
        temp=self.searc(p)
        
        temp.next=temp.next.next

    def printlist(self):
        """ Print all the elements of a list in a row."""
        self.temp=ListNode('a')
        self.temp=self.head.next

        while self.temp != None :
            
            print (self.temp.value)
            print(self.temp.s)
            self.temp=self.temp.next
        


    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        self.temp=ListNode('a')
        self.temp=self.head
        c=-1
        while self.temp.next!=None :
            self.temp=self.temp.next
            c=c+1
            if self.temp.s == x :
                return c
        return c

    def searc(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        self.temp=ListNode('a')
        self.temp=self.head
        while self.temp.next!=None :
            
            if self.temp.next.s == x :
                return self.temp
            self.temp=self.temp.next
        return self.head



    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        self.temp=ListNode('a')
        self.temp=self.head.next
        
        self.count=0
        while self.temp!=None:
                self.count=self.count+1
                self.temp=self.temp.next
            
        return self.count


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,s):
        self.value=0
        self.s=s
        self.next=None

class HashTable :

    def __init__(self) :

        self.T=[None for i in range(30)]
        
        for i in range (0,30):
            self.T[i]=LinkedList()

    def ins(self,s) :
        x=s
        n=len(x)
        k=0
        for i in range(0,n) :

            k=k+ord(x[i])

        h_k=k % 30


        print('the list in T[',h_k,'] is')
        self.T[h_k].insert(k,s)
        self.T[h_k].printlist()


    def dele(self,s) :

        x=s
        n=len(x)
        k=0
        for i in range(0,n) :

            k=k+ord(x[i])

        h_k=k % 30
        self.T[h_k].delete(s)
        print('the list in T[',h_k,'] is')
        self.T[h_k].printlist()
        


    def sear(self,s) :

        x=s
        n=len(x)
        k=0
        for i in range(0,n) :

            k=k+ord(x[i])

        h_k=k % 30

        
        print('the string',s,'is present in',h_k,'th column of hash table and in the following position of linked list')
        return self.T[h_k].search(k)


        
        
    


def main():

    h=HashTable()

    h.ins('apple')

    h.ins('ball')

    h.ins('cat')

    h.ins('act')

    h.ins('tac')
    
    h.ins('atc')

    print(h.sear('cat'))
    
    h.dele('tac')
    
    

if __name__ == '__main__':
    main()
