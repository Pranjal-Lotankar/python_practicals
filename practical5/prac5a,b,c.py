#a. Write a Python script to sort (ascending and descending) a dictionary by value.
released={'Python 3.6': 2017,'Python 1.0': 2002, 'Python 2.3': 2010}
for key,value in sorted(released.items()):
	print (key,value)

print (sorted(released))

'''b. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
print (dic1)
dic1.update(dic3)
print (dic1)

#c. Write a Python program to sum all the items in a dictionary.
d= {'One':10,'Two':20,'Three':30}
print(sum(d.values()))
