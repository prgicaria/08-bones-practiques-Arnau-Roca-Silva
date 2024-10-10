"""
Programa per demanar valors enters per al divisor i el dividend, i calcular el quocient i el residu de la divisió.
Autor: [Arnau Roca Silva]
Data: [2024/10/10]
"""
# Demanem valors enters per a divisor i dividend:

dividend  =int(input("Introdueix el dividend: "))
divisor=int(input("Introdueix el divisor: "))

#Calculem el residu i el quocient:
residu = dividend%divisor
quocient = dividend//divisor

#Mostrem per pantalla de manera ordenada:
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")