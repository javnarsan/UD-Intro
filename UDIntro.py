#RELACION 1
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



a=input("Introduzca una cadena de texto con numeros\n")
b=input("Introduzca un caracter por el que quiera sustituir los numeros\n")
for i in a:
    if(i.isdigit()):
        a = a.replace(i,b)
print(a)
'''

#Ejercicio 6

'''
6. Crear un programa que lea por teclado una cadena y un carácter,
 e inserte el carácter cada 3 dígitos en la cadena.
  Ej. 2552552550 y . debería devolver 255.255.255.0

a=input("Introduzca un número\n")
b=input("Introduzca un caracter que quiera intercalar cada 3 dígitos\n")
c=""
for i in range(0,len(a)):
    c=c+a[i]
    if((i+1)%3==0 and i!=len(a)-1):
        c=c+b
print(c)
'''

#Ejercicio 7

'''
7. Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

- La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.

- Dicha cadena con la primera letra de cada palabra en mayúsculas. 
Por ejemplo, si recibe república argentina debe devolver República Argentina.



a=input("Escriba una cadena de texto\n")
b=""
c=""
d=a.split(" ")
for i in range (len(d)):
    b=b+((d[i])[0]).capitalize()
    for j in range(len((d[i]))):
        if(j==0):
            c=c+" "+(d[i])[j].capitalize()
        else:
            c=c+(d[i])[j]

print("Siglas: \n",b)
print("La misma cadena pero con la primera letra de cada palabra en mayus:\n",c)

'''

#Ejercicio 8

'''
8. Escribe una función es_par que tome un número x como entrada y 
devuelva True si x es par y False si no lo es.

a=4
def es_par(x):
    if(x%2==0):
        return True
    else:
        return False
print(es_par(a))
'''

#Ejercicio 9

'''
9. Escribe una función factorial que tome como entrada un entero x y devuelva el factorial de ese número.


def factorial(x):
    res=1
    for i in range(1,x+1):
        res*=i
    return res
print(factorial(5))
'''

#Ejercicio 10

'''
10. Escribe una función es_primo que tome un número x como entrada y devuelva el booleano True si x es primo y False si no lo es.

def es_primo(x):
    for i in range(2,x):
        if(x%i==0):
            return False
        elif(i==x-1):
            return True
            
print(es_primo(104729))

'''

#Ejercicio 11

'''
11. Escribe una función anti_vocal que tome como entrada un string texto y devuelva el texto sin las vocales.

a="murcielago"
def isVowel(char):
    if char == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
        return True
    else:
        return False
def anti_vocal(x):
    for i in x:
        if(isVowel(i)):
            x=x.replace(i,"")
print(anti_vocal(a))

No funciona, habria que arreglaro
'''

#RELACION 2

#Ejercicio 1

'''
1.  Realiza un módulo que haga operaciones aritméticas entre dos números
(suma, resta, producto, división). 
A continuación, en otro fichero, importa el módulo y prueba alguna de las operaciones anteriores.

import FuncionesAritmeticas

a=45
b=12

print(FuncionesAritmeticas.suma(a,b))
print(FuncionesAritmeticas.resta(a,b))
print(FuncionesAritmeticas.producto(a,b))
print(FuncionesAritmeticas.division(a,b))

'''

#Ejercicio 2

'''
2. Imprime el directorio actual de trabajo.

import os
os.getcwd()
'''

#Ejercicio 3

'''
3. Pide por teclado un directorio de tu disco duro y elimínalo.

from os import rmdir,mkdir
#mkdir("C:/Users/beris/OneDrive/Escritorio/DAM/borrar")
#rmdir("C:/Users/beris/OneDrive/Escritorio/DAM/borrar")
'''

#Ejercicio 4

'''
4. Copia un directorio de tu disco duro a otra ubicación

import shutil,os
os.mkdir("C:/Users/beris/OneDrive/Escritorio/DAM/borrar")
shutil.move("C:/Users/beris/OneDrive/Escritorio/DAM/borrar","C:/Users/beris/OneDrive/Escritorio")
'''

#Ejercicio 5


#5. Liste recursivamente el contenido de su directorio de usuario 
#(C:\Users\alumno). Muestre cada ruta en una línea, y etiquete cada una como DIRECTORIO 
#o como FICHERO.

#import os
#ficheros = os.scandir("C:/Users/beris")
#for fichero in ficheros:
#    if(fichero.is_dir()):
#        print(fichero.name," DIRECTORIO")
#    elif(fichero.is_file()):
#        print(fichero.name," FICHERO")


#Ejercicio 6

'''
6.  Liste todos los archivos ejecutables (extensión '.exe') del directorio C:\Windows\system32. 


import os,fnmatch
ficheros = os.scandir("C:/Windows/system32")
for fichero in ficheros:
    if os.path.isfile(fichero):
            if fnmatch.fnmatch(fichero, '*.exe'):
                print(fichero)
'''

#Ejercicio 7

'''
7. Realice un listado de ficheros del directorio C:\windows\system32. 
Almacene en un fichero llamado "listado_windows.txt" la ruta y tamaño de 
cada fichero con el formato siguiente: ruta;tamaño con una linea para cada fichero encontrado. 
'''
import os
a = open("C:/Users/beris/OneDrive/Escritorio/DAM/ficheroTexto.txt", "w")
for path, subdirs, files in os.walk("C:/Windows/system32"):
   for filename in files:
        f = os.path.join(filename)
        a.write(str(f) + os.linesep) 