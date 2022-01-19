def demo(*values):
	'''Variable length arguments.'''
	s=0
	for i in values:
		s=s+i
	print("sum is",s)

print(demo.__doc__)
demo(1,2,3,5)


