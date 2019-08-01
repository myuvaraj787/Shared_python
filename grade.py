




def grade_mark_cal(i):
	if i > 0 and i <=100:
		if i >= 90:
			print ('GRADE A')
		elif i >= 80 and i <= 90:
			print ('GRADE B')
		elif i >=70 and i <= 80:
			print ('GRADE B')
		elif i >=60 and i <= 70:
			print ('GRADE C')
		elif i >=50 and i <= 60:
			print ('GRADE D')
		elif i >=35 and i <= 50:
			print ('GRADE D')
		elif i < 35:
			print ('GRADE F')
	else:
		print('enter valid marks, you  entered ',i)
		
a=int(input('enter the value '))

grade_mark_cal(a)	


'''
i=int(input('enter the value '))

if i >= 90:
	print ('GRADE A')
elif i >= 80 and i <= 90:
	print ('GRADE B')
elif i >=70 and i <= 80:
	print ('GRADE B')
elif i >=60 and i <= 70:
	print ('GRADE C')
elif i >=50 and i <= 60:
	print ('GRADE D')
elif i >=35 and i <= 50:
	print ('GRADE D')
elif i < 35:
	print ('GRADE F')
	
	
def grade_mark_cal(a)	'''