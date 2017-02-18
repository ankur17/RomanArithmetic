from collections import OrderedDict


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

