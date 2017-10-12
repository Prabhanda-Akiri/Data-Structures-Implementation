class Heap:

    def __init__(self):

        self.a=['a',2,6,12,4,10,14,16,23,8,12,11,20,5,18]
        self.last=14

    def insert(self,x):

        self.a.append(x)
        self.last=self.last+1


    def heapifydown(self):

        
        for i in range(1,self.last+1):

            p=2*i+1
            q=2*i

            if p<=self.last:

                if self.a[p]>self.a[q]:
                    if self.a[p]>self.a[i]:
                        temp=self.a[p]
                        self.a[p]=self.a[i]
                        self.a[i]=temp

                elif self.a[q]>self.a[p]:
                    if self.a[q]>self.a[i]:
                        temp=self.a[q]
                        self.a[q]=self.a[i]
                        self.a[i]=temp
            elif q<=self.last:

                if self.a[q]>self.a[i]:
                        temp=self.a[q]
                        self.a[q]=self.a[i]
                        self.a[i]=temp




    def heapifyup(self):

        for i in range(self.last,1,-1):

            if i%2==0:
                p=i/2
            else:
                p=(i-1)/2
            k=int(p)

            if self.a[k]<self.a[i]:

                temp=self.a[k]
                self.a[k]=self.a[i]
                self.a[i]=temp




        
    def maximum(self):

        return self.a[1]

    def extractmax(self):

        m=self.a[1]
        self.a[1]=self.a[self.last]
        self.last=self.last-1
        self.heapifyup()
        self.heapifydown()
        return m


    def buildheap(self):

        self.heapifyup()
        self.heapifydown()



    def list(self):

        print(self.a[1:self.last+1])



class PriorityQueue:

    def __init__(self):

        self.Qu=Heap()

    def ins(self,a):

        self.Qu.insert(a)

    def build(self):

        self.Qu.buildheap()

    def max(self):
        print('maximum is:',self.Qu.maximum())

    def printlist(self):
        
        self.Qu.list()
    def exmax(self):
        print('Maximum extracted ',self.Qu.extractmax())
def main():

    A=['2','6','12','4','10','14','16','23','8','12','11','20','5','18']
    h=PriorityQueue()
    h.ins(19)
    h.build()
    print('Heapified Queue:')
    h.printlist()
    h.max()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    h.exmax()
    print('Now the Queue is:')
    h.printlist()
    



if __name__ == '__main__':
    main()
