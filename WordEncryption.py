''' This program will do an encryption/decryption'''

#the ord and chr will be used 

plainText = input("Enter a one-word,lowercase message:")
distance = int(input("Enter the distance value:"))
code = ""

for ch in plainText :
	ordvalue = ord(ch)
	ciphervalue = ordvalue + distance
	if ciphervalue > ord('z'):
		ciphervalue = ord('a') + distance-\
						(ord('Z') - ordvalue +1)

	code += chr(ciphervalue)
print(code)

