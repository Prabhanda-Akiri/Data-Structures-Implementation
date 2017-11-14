
def main():

	A=[3,5,6,7,2,4,8,9]

	low=0
	high=7

	print('Array before sorted:',A)

	QuickSort(A,low,high)

	print('\n\nArray after sorted:\n','                 ',A)


def QuickSort(A,low,high):

	if low<high:

		q=Partition(A,low,high)

		QuickSort(A,low,q-1)
		QuickSort(A,q+1,high)


def Partition(A,low,high):

	i=low-1

	x=A[high]

	for j in range(low,high):

		if A[j]<=x:

			A[i+1],A[j]=A[j],A[i+1]

			i=i+1

	A[i+1],A[high]=A[high],A[i+1]

	return i+1


if __name__ == '__main__':
	main()
