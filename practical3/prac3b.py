'''Take a list, say for example this one:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that
prints out all the elements of the list that are less than 5.'''

l1=[1,1,2,3,5,8,13,21,34,55,89]
l2=[]
for x in l1:
    if x < 5:
        l2.append(x)
        print(l2)