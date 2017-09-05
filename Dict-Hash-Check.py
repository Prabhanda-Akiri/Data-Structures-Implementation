#takes n number of words as input and checks the spellings

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
        return -1

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
        
        h_k=hash(s)%30

        self.T[h_k].insert(hash(s),s)
        


    def dele(self,s) :

    
        h_k=hash(s) % 30
        self.T[h_k].delete(s)
        print('the list in T[',h_k,'] is')
        self.T[h_k].printlist()
        


    def sear(self,s) :

        
        h_k = hash(s) % 30
        return self.T[h_k].search(s)
        
        
    def check(self,s) :
        
        
        if self.sear(s) == -1 :
            print('the word',s,'is mispelled')
            
        else :
            print('the word',s,'is spelled correctly')
        
    

def main():

    h=HashTable()
    
    n=341

    for i in range(n):
        x=input()
        h.ins(x)
        
    h.check('available')
    
def hash(s):
    
    n=len(s)
    x=33
    k=ord(s[n-1])
    for i in range(n-2,-1,-1):
        
        k=ord(s[i]) + (x*k)
        
    return k
        
        
        
        
    

if __name__ == '__main__':
    main()
