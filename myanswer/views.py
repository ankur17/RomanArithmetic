from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# import sys
# sys.path.append('Utils')
# from Utils.test import RomToNum,NumtoRom


##################################
from collections import OrderedDict

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


rom_val = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")]
def NumtoRom(input):
	dIntRoman = OrderedDict(rom_val)
    	
	def roman_num(num):
		for r in dIntRoman.keys():
			x, y = divmod(num, r)
			yield dIntRoman[r] * x
			num -= (r * x)
			if num > 0:
				roman_num(num)
			else:
				break
	
	return "".join([a for a in roman_num(input)])

def evaluat(input1,input2,Operation):
	if Operation=='1':
		return "Sum: " + str(NumtoRom(RomToNum(input1) + RomToNum(input2)))
	if Operation=='2':
		return "Diff: " + str(NumtoRom(RomToNum(input1) - RomToNum(input2)))
	if Operation=='3':
		return "Product: " + str(NumtoRom(RomToNum(input1) * RomToNum(input2)))
	if Operation=='4':
		return "Quotient: "+ str(NumtoRom(RomToNum(input1) / RomToNum(input2)))

##################################
def basic(request):
	t = loader.get_template('myanswer/basic.html')
	c = dict()
	if 'list' in request.POST:
		c['input1'] = request.POST['OneInput']
		c['input2'] = request.POST['TwoInput']
		c['OpValue'] = request.POST['Operation']
		c['Result'] = evaluat(c['input1'],c['input2'],c['OpValue'])

	else:
		c['Result'] = 'Your Answer here'
	return HttpResponse(t.render(c, request))

