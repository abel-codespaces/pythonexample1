print("Hola, soy un programa de Python muy sencillo")
print("En este programa, te voy a demostrar algunas funciones de Python")
print("En primer vamos a usar la función sum() y vamos a sumar varios números")
print("Vamos a sumar 3 números:")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input ("Introduce el tercer número: "))
resultado = sum([num1, num2, num3]) # sum() recibe una lista de números
print(f"La suma de {num1}, {num2} y {num3} es {resultado}") # se muestra el resultado
print(" ")
print("Ahora vamos a usar la función max() para obtener el número mayor")
print("Voy a comparar los números que introdujiste y te diré cuál es el mayor")
max_num = max(num1, num2, num3) # max() recibe una lista de números
print(f"El número mayor entre {num1}, {num2} y {num3} es {max_num}") # se muestra el resultado
print(" ")
print("Por último, vamos a usar la función min() para obtener el número menor")
print("Voy a comparar los números que introdujiste y te diré cuál es el menor")
min_num = min(num1, num2, num3) # min() recibe una lista de números
print(f"El número menor entre {num1}, {num2} y {num3} es {min_num}") # se muestra el resultado
print(" ")
print("¡Eso es todo! Espero que te haya gustado este programa. ¡Hasta luego!") # se despide el programa
print("Nota: este programa usó las funciones print(), input(), float(), sum(), max() y min()") # se muestra una nota al final del programa