# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# replace whitespace with %20
def replaceSpace(A):
	i = 0
	newString = []
	while i < len(A):
		if A[i] != ' ':
			newString.append(A[i])
		else:
			newString.append('%20')
		i = i + 1
	return ''.join(newString)

if __name__ in '__main__':
	print(replaceSpace("Ather is cool"))




