#day-2 24/10/22
#sorting algorithm

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [10,30,2,40,5]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)


#day-2 24/10/22
#remove duplicate elements
given_array=[10,20,10,30,20]
print("before removal of duplicate",given_array)
remove_duplicate=[]
for i in given_array:
    if i not in remove_duplicate:
        remove_duplicate.append(i)
print("After removal of duplicate",remove_duplicate)

#day-2 24/10/22
#reverse a array elements
revers=[10,20,30,40]
print("before_reverse",revers)
revers.reverse()
print("after_reverse",revers)

#day-2 24/10/22
#finding missing numbers from 1 to 100
integer=[14,5,6,78,9,2,3]
miss_int=[]
for i in range(1,101):
    if i not in integer:
        miss_int.append(i)
print("missing numbers are",miss_int)

#day-2 24/10/22
#finding duplicate numbers from a array
dup_ele=[1,2,3,4,1,2]
print("duplicate numbers are")
for i in range(0,len(dup_ele)):
    for j in range(i+1,len(dup_ele)):
        if(dup_ele[i]==dup_ele[j]):
            print(dup_ele[j],end=" ")









