# multiplo de 3
'''
numero = int(input("digite un numero entero: "))
modulo = numero % 3 
print(f'el modulo del numero es: {modulo}')
'''

# condiciones de python 

# if()

sensorNivelAgua=int(input("digite el nivel de agua actual: "))

if(sensorNivelAgua>=0 and sensorNivelAgua<20):
    print(f'peligro el nivel {sensorNivelAgua} es peligroso')
elif(sensorNivelAgua>=20 and sensorNivelAgua<400):
    print(f'hidroituango funcionando ok {sensorNivelAgua}')
elif(sensorNivelAgua>=400):
    print(f'peligro el nivel {sensorNivelAgua} es peligroso')
else:
    print(f'el nivel del agua no es valido')