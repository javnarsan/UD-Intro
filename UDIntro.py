#Ejercicio 2, ultima parte
'''
Crear un programa que lea por teclado una cadena, y muestre la siguiente información:
1.	Imprima los dos primeros caracteres.
2.	Imprima los tres últimos caracteres.
3.	Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
4.	Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh 


print("Introduzca una cadena de texto")
a=input()
#print(a[0:2])
#print(a[-3:])
b = ""
c = ""
for i in range(0,len(a),2):
    b+=a[i]
print(b)
for i in range(0,len(a)):
    c=a[i]+c
print(c)
'''

#Ejercicio 3

'''
3. Crear un programa que lea por teclado una cadena y un carácter,
 e inserte el carácter entre cada letra de la cadena. 
 Ej: separar y , debería devolver s,e,p,a,r,a,r

print("Introduzca una cadena de texto")
a=input()
b = ""
for i in range(0,len(a)):
    b+=a[i]
    if(i!=len(a)-1):
        b+=","
print(b)

'''

#Ejercicio 4

'''
4. Crear un programa que lea por teclado una cadena y un carácter,
 y reemplace todos los espacios por el carácter. 
 Ej: mi archivo de texto.txt y _ debería devolver mi_archivo_de_texto.txt


print("Introduzca una cadena de texto con espacios")
a=input()
print("Introduzca un caracter por el que quiera sustituir los espacios")
b=input()
a=a.replace(' ',b)
print(a)
'''

#Ejercicio 5

'''
5. Crear un programa que lea por teclado una cadena y un carácter,
 y reemplace todos los dígitos en la cadena por el carácter.
  Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
'''


a=input("Introduzca una cadena de texto con numeros\n")
b=input("Introduzca un caracter por el que quiera sustituir los numeros\n")

for i in a:
    if(i.isdigit):
        a = a.replace(i,b)
print(a)
