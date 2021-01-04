#nthlargestorsmallest

# so according to this question we have to write the logic so that we can find out the 
#kth biggest number in the list


a = [1,22,334,22,44,22,11,2223,2234,2234]

k = int(input("Enter the Kth value to find in the array."))

x = sorted(a)
print(x)
print(x[-k])

