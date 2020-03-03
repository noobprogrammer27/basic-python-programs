#here load all the needed special characters and unwanted symbols.
special=[';', ':', '!', "*",'@','#','&','%'] 
l1=[]
test_string = "infosys@337"#enter your own input here
#if you want to take the input from user use below code 
#test_string=input()
for i in special : 
	test_string = test_string.replace(i,'') 
	#here we are replacing specialcharacters with i
print(test_string)
