#Define a function that computes the length of a given list or string.

def len(s):
	count = 0
	for i in s:
		if i != ' ':
			count += 1
	return count

print('The total length of the string is: ', count)
ustr=input()
len(ustr)
