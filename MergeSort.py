def main():

    A=[3,5,6,7,2,4,8,9]

    low=0
    high=7

    print('Array before sorted:',A)
    mergesort(A,low,high)
    print('\n\nArray after sorted:\n','                 ',A)



def mergesort(A,low,high):

    if low<high:

        mid=int((low+high-1)/2)

        mergesort(A,low,mid)
        mergesort(A,mid+1,high)

        if(not high==low+1):
            merge(A,low,mid,high)

    return

def merge(A,low,mid,high):

    n1=mid-low+1
    n2=high-mid
    L=[]
    R=[]
    for i in range(0,n1):

        L.append(A[low+i])

    for i in range(0,n2):

        R.append(A[mid+1+i])

    l=0
    r=0
    i=low

    while(l<n1 and r<n2):

        if L[l]> R[r]:

            A[i]=R[r]
            r=r+1

        else:

            A[i]=L[l]
            l=l+1

        i=i+1

    
    while l<n1:

        A[i]=L[l]
        l=l+1
        i=i+1                   

    while r<n2:

        A[i]=R[r]
        r=r+1
        i=i+1


if __name__ == '__main__':
    main()
