empty_list= [ ]
print(empty_list)

marks= [100, 90, 87, 85, 95]
print("Marks:", marks)

sample_list= [67, 89, 94]*2
print("Repeated sample works:",sample_list)

length = len(marks)
print("Total numbers of marks:", length)

print("First mark of the list:", marks[0])
print("Second mark of the list:", marks[-1])

print("First three marks of the list are:", marks[0:3])

print("Reverse of the list will be:",marks[::-1])

def match_marks(mark_list):
    count= 0
    matched_marks= []
    for mark in mark_list:
        mark_text= str(mark)

        if len(mark_text)>1 and mark_text[0] == mark_text[-1]:
            count + count+1
            matched_marks.append(mark)

    print("Marks with first and last digit same are:", matched_marks)
    return count

same_digit_count= match_marks([54, 54, 76, 85, 92])
print("Number of matching marks:", same_digit_count)

total= 0

for mark in marks:
    total+=mark

average= total/len( marks)

print("Sum of makrs:", total)
print("Average marks:", average)

marks.sort()

print("The smallest number is:", marks[0])
print("The largest number is:", marks[-1])

print()
print("===STUDENT MARK ANALYZER===")    
print("Sorted marks:", marks)
print("Total marks:", total)
print("Average marks:", average)
print("Lowest marks:", marks[0])
print("Highest mark:", marks[-1])
print("==========================")