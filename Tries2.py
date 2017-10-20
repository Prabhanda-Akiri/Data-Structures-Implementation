class TrieNode:

    def __init__(self):

        self.val=None
        self.children=[]
        self.isEndofWrd=[]

class Trie:

    def __init__(self):

        self.root=TrieNode()

    
    def sear(self,x,a):

        for i in range(len(x.children)):

            if x.children[i].val==a:

                return i

        return 


    def insert(self,x,l):

        temp=self.root
        n=len(x)

        for i in range(n):


            k=self.sear(temp,x[i])

            if k!=None:
                temp=temp.children[k]

            else:

                temp.children.append(TrieNode())
                temp.children[-1].val=x[i]
                
                temp=temp.children[-1]
                

        temp.isEndofWrd.append(l)

    
    def search(self,x):

        n=len(x)
        temp=self.root
        p=0
        for i in range(n):

            k=self.sear(temp,x[i])

            if k!=None:
                temp=temp.children[k]
            else:
                p=2
                break

        if p==2:
            print('\nThe word ',x,' is not present in the tree')
            return
        else:
            print('\nThe word ',x,' exists and is present at indices ',temp.isEndofWrd[:])



    def traversal(self,x):

        if len(x.children)==0:

            print(x.val)
            return

        else:
            print(x.val)
            for i in range(len(x.children)):

                self.traversal(x.children[i])





def main():

    T='she sells sea shells on sea shore she went to see sea'
    S=T.split(" ")
    print('The text inserted is:\n')
    print(T)

    st=Trie()
    k=1
    for i in range(len(S)):

        st.insert(S[i],k)
        k=k+len(S[i])+1

    #st.traversal(st.root)
    
    s=input('\nEnter your word to be searched among the inserted words:\n\n')

    st.search(s)

if __name__ == '__main__':
    main()
