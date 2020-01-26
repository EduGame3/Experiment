print('COMPARADOR DE NÚMEROS')
a = float(input('Escriba un número: ')) #¿cómo hacer para que acepte el 1/2?
b = float(input('Escriba otro número: '))
if (a < b):
	print(f"Menor: {a} ; Mayor: {b}")
elif (a > b):
	print(f"Menor: {b} ; Mayor: {a}")
else:
	print('Los dos números son iguales')
