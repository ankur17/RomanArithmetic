from NumtoRom import *
from RomtoNum import *

def evaluat(input1,input2,Operation):
	if Operation=='1':
		return "Sum: " + str(NumtoRom(RomToNum(input1) + RomToNum(input2)))
	if Operation=='2':
		return "Diff: " + str(NumtoRom(RomToNum(input1) - RomToNum(input2)))
	if Operation=='3':
		return "Product: " + str(NumtoRom(RomToNum(input1) * RomToNum(input2)))
	if Operation=='4':
		return "Quotient: "+ str(NumtoRom(RomToNum(input1) / RomToNum(input2)))
