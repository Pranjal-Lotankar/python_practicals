'''C. Write a Python program to clone or copy a list'''

l1=[2, 4, 7, 8, 9, 0]
print ("Original List is", l1)
l2=l1
print ("Clone List is ",l2)

old_list = [1, 2, 3]
new_list = old_list

new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)


my_list = ['cat', 0, 6.7]
new_list = my_list.copy()
print('Copied List:', new_list)