



texto_1 = "ana"
texto_2 = "barrilete cosmico"
texto_3 = "yo hago yoga hoy"
texto_4 = "arriba la birra"
texto_5 = "arriba la barra"


def es_polindromo(datosRec):
    return datosRec == datosRec[::-1]


datos = [texto_1, texto_2, texto_3, texto_4, texto_5]
datos2 = [texto_1.replace(' ',''), texto_2.replace(' ',''), texto_3.replace(' ',''), texto_4.replace(' ',''), texto_5.replace(' ','')]


print("\n\nCon espacios\n")

for x in datos:
    print(x + "->" + str(es_polindromo(x)) )


print("\n\nSin espacios\n")

for x in datos2:
    print(x + "->" + str(es_polindromo(x)) )


#assert es_polindromo(texto_1) == True, "Fallo"

def F_n(n):
    # sigamos la definición de la secuencia de Fibonacci
    if n == 0: # Si n es 0 entonces devuelvo 0 
        return 0
    if n == 1:
        return 1 # Si n es 1 entonces devuelvo 1
    else:
        return F_n(n-1) + F_n(n-2) # En cualquier otro caso devuelvo la suma de los dos números de Fibonacci preivos


# Fibonacci
print([F_n(x) for x in range(0,25)])


n = 1
print(F_n(1-1) + F_n(1-2))