#!/usr/bin/env python

'''bones_practiques. Demana
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Descripció llarga del programa. Indicar que fa el
programa i el resultat esperat.
'''
__author__ = "Arnau Roca Silva"
__email__ = "aroca@instituticaria.cat"
__date__ = "2024/10/10"
# Demanem valors enters per a divisor i dividend:

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))

# Calculem el residu i el quocient:
residu = dividend % divisor
quocient = dividend//divisor

# Mostrem per pantalla de manera ordenada:
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
