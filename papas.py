
#ejercicio de papas

valor_peso=float(input("¿Cual es el gramaje de sus papas?(grs):  "))

valor_precio=float(input("¿Cual es el valor de las papas por kilogramo?):   "))

valor_peso2=valor_peso/1000

valor_total = (valor_precio * valor_peso2)

print("Tendra que pagar: ", valor_total)

extra = input("Le convence lo que debe pagar? (SI/NO):  ")

if extra=="SI":
    print("Me alegro pr ello, tenga un buen dia")
else:
    if extra=="NO":
        print("Lamentable quejese de la inflacion")

    