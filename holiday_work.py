#(22/10/22)
#how do you find missing number in a given array from 1 to 100
arr=[]
total=int(input("Enter number of elementes"))
for i in range(0,total):
    numbers=int(input("Enter your numbers one by one"))
    arr.append(numbers)
print("The numbers you enter",arr)

miss=[]
for j in range(1,101):
    if j not in arr:
        miss.append(j)
print("Missing numbers in array are",miss)


#(22/10/22)
#how do yo find duplicate numbers from a given array

find_dup=[]
dup=int(input("Enter total elements or value"))
for get in range(0,dup):
    dup_ele=int(input("Enter value"))
    find_dup.append(dup_ele)
print("Array elements are ",find_dup)
print("Duplicate elements")
for di in range(0,len(find_dup)):
    for dj in range(di+1,len(find_dup)):
        if(find_dup[di]==find_dup[dj]):
            print(find_dup[di])


#(22/10/22)
#how do yo find largest number in a unsorted list
flag=0
large_array=[1,2000,400,20]
large_array.sort()
print("Smallest number",large_array[0])
print("Largest number",large_array[-1])


#(22/10/22)
#how do you find all pair of integers whose sum is equal to given number

pair_array=100
def my_sum(s):
    print("all pair of integers are")
    for i in range(0,pair_array):
        for j in range(i,pair_array):
            for k in range(i,pair_array):
                if i+j+k==s:
                    print([i,j,k],end=" ")
                
sum=int(input("Enter number for finding pair of numbers"))                
my_sum(sum)



#(22/10/22)
#how do you remove duplicates in array

ar=[1,2,1,2]
print("array before duplicate identify",ar)
temp=[]

for i in ar:
    if i not in temp:
        temp.append(i)
        ar=temp
print("array after duplicate identify",ar)












