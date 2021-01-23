#thedutchflagproblem
#  so here we have the array having three kinds of numbers and we have to sort them without using any
#  sorting algorithm
a = [1,1,1,0,0,0,2,2,2,0,0,0,0,0]
#we have to sort in in a manner. Without using the sorting technique.
low = 0
mid = 0
high = len(a)-1
while mid <= high:
	if a[mid] == 0:
		a[mid],a[low] = a[low],a[mid]
		mid += 1
		low += 1

	elif a[mid] == 1:
		mid += 1
	else:
		a[mid],a[high] = a[high],a[mid]
		high -= high
print(a)
