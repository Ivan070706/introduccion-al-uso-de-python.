def main (): 
    #5.2
    lista1 = ["Manzana", "Pera", "Melocoton"]

    #5.3
    lista2 = ["Kiwi","Sandía","Melón"]

    #5.4
    lista1.extend(lista2)

    # 5.5
    print("Ultimo:", lista1[-1])

    #5.6
    tupla_valor = (3,5,7)

    #5.7
    print("primero tupla:" , tupla_valor[0])

    # 5.8
    inicio = int(input("Introduce el inicio: "))
    fin = int(input("Introduce el fin: "))
    salto = int(input("Introduce el salto: "))

    #rango
    rango = range(inicio, fin, salto)

    # 5.9
    print("Rango:", list(rango))
    
if __name__ == "__main__":
        main()
    