#Find the maximum and minimum element in an array
a = [1,2,3,4,5,6,7,7,89]

for i in range(0,len(a)-2):
	if a[i] < a[i+1]:
		i += 1
	if a[i] >= a[i+1]:
		a[i],a[i+1] = a[i+1],a[i]
		i += 1
print(a[-1])