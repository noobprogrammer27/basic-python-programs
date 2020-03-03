def mini(S1, S2): 
	n1=len(S1)#here we are getting length of the string
	n2=len(S2) 
	count=100
	for i in range(n2-n1+1): 
		Rem=0 
		for j in range(n1): 
			if (S1[j]==S2[i+j]): #comparing one character with other string character
				break
			else:
				Rem+= 1
		count=min(Rem,count)#if the comparison fails it increases the count 
	return count
S1=input()#enter your own string or let it be like that
S2=input()#enter your own string or let it be like that
print(mini(S1, S2))
