# Esercizio lista numeri


uas = int(input("Dimmi il numero minore: "))
sata = int(input("Dimmi il numero maggiore: "))

for i in range(uas, sata+1):
	if not i%7: 
		print('Buzz')
	else: 
		print(i) 

print(sum(range(uas, sata + 1)))