L= [1,2,3,4,5,6,7,8,9,0]
print("Original List=", L)

count= 0
for i in L:
    count+=i

average= count/len(L)
print("Sum:", count)
print("Average:", average)

L.sort()
print("The list after sorting is:", L)
print("Smallest number is:", L[0])
print("Largest number is:", L[9])  