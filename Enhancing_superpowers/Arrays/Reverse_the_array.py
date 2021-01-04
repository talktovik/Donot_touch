#Reversing the array.
#infact there is a function which can directly reverse the array. 

#let say we have a list which we want to reverse.

#let the list be list1 
list1 = [1,2,3,4,5] 
# we need the output as [5,4,3,2,1]

#for that we can use the very trival concept which is : 


# lens = len(list1)
# for i in range(0,lens/2):
# 	temp = list1[i]
# 	list1[i] = list1[lens-i]
# 	list1[lens-i] = list[i]

# print(list1) 


# this is showing out of range index
# let me use a while loop for better results 
# i = 0
# j = len(list1)
# while(i<j):
# 	temp = list1[j-1]
# 	list1[j] = list1[i]
# 	list1[i] = temp
# 	i += 1
# 	j -= 1

# print(list1)
# again this is out of index.

# now lets modify the code and really make a algorithm	


lens = len(list1)
for i in range(0,lens/2):
	temp = list1[lens-i-1]
	list1[lens-i-1] = list1[i]
	list1[i] = temp

print(list1) 


# and it fucking worked.

# Tip of the day. ALWAYS MAKE A LOGIC IN MIND BEFORE DIRECTLY JUMPING ON THE PROBLEM.
















