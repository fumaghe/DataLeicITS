# Esercizio lista numeri


min = int(input("Dimmi il numero minore: "))
max = int(input("Dimmi il numero maggiore: "))

for i in range(min, max+1):
	if not i%7: 
		print('Buzz')
	else: 
		print(i) 

print(sum([i for i in range(min, max + 1)]))