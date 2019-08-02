def donuts(count):
  # +++your code here+++
	#count=s
	if count > 10:
		a="donuts ({0}) returns Number of donuts: many".format(count)
	else:
		a="donuts({0}) returns Number of donuts: {0}".format(count)
	#print(a)
	return a

	
a=donuts(int(input()))
print(a)

'''
def donuts(count):
  # +++your code here+++
  # LAB(begin solution)
  if count < 10:
    return 'Number of donuts: ' + str(count)
  else:
    return 'Number of donuts: many'
	
	'''