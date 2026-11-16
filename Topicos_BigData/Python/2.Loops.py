print("Estructuras Repetitivas")

#for
for i in range (1,11):
    print(f'Numero {i}')

for letra in ("Hola Mundo"):
    print(letra)
#while
contador=1
while contador <= 3:
    print(f'Intento {contador}')
    contador += 1 #Contador = Contador + 1
    
# Do while
while True:
    numero=int(input("Ingrese un numero mayor 0: "))

    if numero > 0:
        break