''' Binary to Dec'''

bitString = input("Enter a string of bits:")
decimal = 0
exponent = len(bitString) - 1

for count in bitString :
	decimal = decimal + int(count) * 2 ** exponent
	exponent -= 1
print("The integer value of" , str(bitString), "is:" , str(decimal))