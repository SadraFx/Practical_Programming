def evanishoroddish(n):
	listN = []
	for i in str(n):
		intN = eval(i)
		listN.append(intN)
     
	sumN = sum(listN)
	if sumN % 2 == 0:
		print("Evanish")
	else:
		print("Oddish")
  
evanishoroddish(11)
evanishoroddish(12)
evanishoroddish(13)
evanishoroddish(14)


