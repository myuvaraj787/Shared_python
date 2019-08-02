def match_ends(a):
	print(a)
	cnt =0
	for i in a:		
		if len(i) > 3 and i[0] == i[-1]:
			cnt+=1
	return (cnt)

a=['ananda','balab','if','endif']
print(match_ends(a))


