


'''

def donuts(count):
  # +++your code here+++
	#count=s
	if count > 10:
		a="donuts({0}) returns Number of donuts: many".format(count)
	else:
		a="donuts({0}) returns Number of donuts: {0}".format(count)
	#print(a)
	return a

	
a=donuts(int(input()))
print(a)
'''

'''
print ('both_ends')

def both_ends(s):
	if len(s) > 2:
		str1=s[0:2]
		str2=s[-2:]
		print(str1 + str2)
		return str1 + str2
	else:
		return ''
	
  # +++your code here+++
	#return (str1+str2)
  
a=(both_ends('GOPALRAMASAMY'))
print(a)
'''

'''
	
def fix_start(s):
  # +++your code here+++
	front = s[0]
	back = s[1:]
	fixed_back = back.replace(front, '*')
	return front + fixed_back

print(fix_start('GOPALGOPALGOPALGGGGGGGGGGGGgggg'))	

'''
'''
def mix_up(a, b):
  # +++your code here+++
  str1=a
  str2=b
  
  print( b + ' ' + a)
  a_swapped = b[:2] + a[2:]
  b_swapped = a[:2] + b[2:]
  
  c= a_swapped + ' ' + b_swapped 
  
  return c

print(mix_up('GOPAL', 'RAM'))
'''
