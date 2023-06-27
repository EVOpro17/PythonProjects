''' Data Decryption'''

kode = input("gee die kode:")
afstand = int(input("gee die afstand:"))
woord = ""

for char in kode:
	ordWaarde = ord(char)
	kodeWaarde = ordWaarde - afstand
	if kodeWaarde < ord('a') :
		kodeWaarde =  ord('z') - (afstand -(ord('a') - kodeWaarde ))
	woord += chr(kodeWaarde)
print(woord)
