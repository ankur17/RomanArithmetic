d_Ranks = {'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000}
def RomToNum(inp):
	
	
	ans = 0
	token = [d_Ranks[a] for a in inp]
	for index in range(len(token)-1):
		if token[index]>= token[index+1]:
			ans = ans+token[index]
		else:
			ans = ans-token[index]
		
	return ans + token[-1]
