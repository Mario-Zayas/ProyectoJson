from funcion import *
categorias = []
opcion = menu()
while opcion != 6:
    if opcion == 1:
        categorias = listar_categorias()
    elif opcion == 2:
        categoria = input("Ingrese la categoria: ")
        print("Hay un total de", contar_armas_por_categoria(categoria, categorias), "armas en la categoría", categoria)
    elif opcion == 3:
        arma = input("Ingrese el arma: ")
        armas_filtradas = filtrar_armas(arma, categorias)
    elif opcion == 4:
        menu_busqueda_armas(categorias)
    elif opcion == 5:
        requisitos_armas(categorias)
    elif opcion == 6:
        print("")
    else:
        print("Opcion no optima, utilice una optima.")
    opcion = menu()



