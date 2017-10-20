class TrieNode:

    def __init__(self):

        self.val=None
        self.children=[]
        self.isEndofWrd=False

class Trie:

    def __init__(self):

        self.root=TrieNode()

    
    def sear(self,x,a):

        for i in range(len(x.children)):

            if x.children[i].val==a:

                return i

        return 


    def insert(self,x):

        temp=self.root
        n=len(x)

        for i in range(n):

            q=self.searc(temp,x[i])

            if q!=None:
                
                s=temp.children[q].val
                if len(s)>1:

                    temp.children[q].val=s[0]
                    temp.children[q].children.append(TrieNode())
                    temp.children[q].children[-1].val=s[1:]
                temp=temp.children[q]

            else:

                temp.children.append(TrieNode())
                temp.children[-1].val=x[i:]
                
                temp=temp.children[-1]
                break
                

        temp.isEndofWrd=True

    
    def searc(self,x,a):

        for i in range(len(x.children)):
            
            if x.children[i].val[0]==a:

                return i       

        return 

    def search(self,x):

        n=len(x)
        temp=self.root
        p=0

        for i in range(n):

            k=self.searc(temp,x[i])

            if k!=None:
                if len(temp.children[k].val)>1:
                    if temp.children[k].val==x[i:]:
                        break
                    else:
                        p=2
                        break
                temp=temp.children[k]
            else:
                p=2
                break

        if p==2:
            print('\nThe word',x,'is not present in the tree')
            return
        else:
            print('\nThe word',x,'exists')



    def traversal(self,x):

        if len(x.children)==0:

            print(x.val)
            return

        else:
            print(x.val)
            for i in range(len(x.children)):

                self.traversal(x.children[i])





def main():

    S=['bear','bell','today','to','bid','bull','buy','sell','stock','stop']

    st=Trie()
    print('\n\nHere are the list of words inserted:\n')
    print(S)

    for i in range(len(S)):

        st.insert(S[i])

    #st.traversal(st.root)
    
    s=input('\nEnter a word to search among the inserted words:\n\n')

    st.search(s)


if __name__ == '__main__':
    main()
