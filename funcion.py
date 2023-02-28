
import json

def menu():
    print("-------------------------------------------")
    print("Proyecto de Json")
    print("\n")
    print("1. Listar las categorias de armas")
    print("2. Contar armas de la categoria")
    print("3. Informacion del arma")
    print("4. Buscar informacion relacionada con el arma")
    print("5. Pedir tus requisitos para el arma")
    print("6. Salir")
    print("\n")
    print("-------------------------------------------")
    opcion=int(input("Seleccione una de las opciones: "))
    return opcion

def listar_categorias():
    with open('armas.json', 'r') as f:
        datos_arma = json.load(f)
    categorias = []
    for arma in datos_arma:
        categorias.append(arma)
    print("Estas son las categorias que hay:")
    for categoria in categorias:
        print("- ", categoria['category'])
    return categorias

def contar_armas_por_categoria(categoria, categorias):
    for arma in categorias:
        if arma['category'] == categoria:
            return len(arma.get('Daggers', [])) + len(arma.get('Straight_Swords', [])) + len(arma.get('Greatswords', [])) + len(arma.get('Ultra_Greatwords', [])) + len(arma.get('Curved_Swords', [])) + len(arma.get('Katanas', [])) + len(arma.get('Curved_Greatswords', [])) + len(arma.get('Piercing_Swords', [])) + len(arma.get('Axes', [])) + len(arma.get('Great_Axes', [])) + len(arma.get('Hammers', [])) + len(arma.get('Great_Hammers', [])) + len(arma.get('Fist_&_Claw', [])) + len(arma.get('Spears', [])) + len(arma.get('Halberds', [])) + len(arma.get('Whips', [])) + len(arma.get('Bows', [])) + len(arma.get('Greatbows', [])) + len(arma.get('Crossbows', [])) + len(arma.get('Flames', [])) + len(arma.get('Catalysts', [])) + len(arma.get('Talismans', []))
    print("No se encontró la categoria")

# Solo funciona con armas con daño fisico que tengan regular y regular +15, si tienen regular +5 o magico no funciona
def filtrar_armas(arma, categorias):
    arma_encantada = []
    for categoria in categorias:
        for arma_categoria in categoria[list(categoria.keys())[1]]:
            if arma_categoria["name"] == arma:
                arma_encantada.append({
                    "name": arma_categoria["name"],
                    "regular_phy_dmg": arma_categoria["regular_phy_dmg"],
                    "regular15_phy_dmg": arma_categoria["regular15_phy_dmg"],
                    "enchantable": arma_categoria["enchantable"]
                })
    for arma in arma_encantada:
        print("Nombre:", arma["name"])
        print("Daño fisico regular: ", arma["regular_phy_dmg"])
        print("Daño fisico regular +15: ", arma["regular15_phy_dmg"])
        print("Encantada: ", arma["enchantable"])
    return arma_encantada

def buscar_info_armas(tipo_info, valor, categorias):
    resultado = []
    for categoria in categorias:
        for arma in categoria[categoria['category']]:
            if tipo_info in arma and arma[tipo_info] == valor:
                resultado.append((arma['name'], categoria['category']))
    return resultado


def menu_busqueda_armas(categorias):
    opcion = input("""
    ¿Que informacion deseas buscar?
    1. Durabilidad
    2. Tipo de ataque
    3. Peso
    4. Salir
     """)
    opcion=int(input("Seleccione una de las opciones: "))
    
    if opcion == '1':
        valor = input("Ingrese la durabilidad del arma: ")
        arma_detalle = buscar_info_armas('durability', int(valor), categorias)
        if len(arma_detalle) == 0:
            print("No se encontraron armas con esa durabilidad")
        else:
            print("Las armas con durabilidad", valor, "son:")
            for arma in arma_detalle:
                print("-", arma[0], "(", arma[1], ")")
        menu_busqueda_armas(categorias)

    elif opcion == '2':
        valor = input("Ingrese el tipo de ataque que desea buscar: ")
        arma_detalle = buscar_info_armas('attack_type', valor, categorias)
        if len(arma_detalle) == 0:
            print("No se encontraron armas con ese tipo de ataque")
        else:
            print("Las armas con tipo de ataque", valor, "son:")
            for arma in arma_detalle:
                print("-", arma[0], "(", arma[1], ")")
        menu_busqueda_armas(categorias)

    elif opcion == '3':
        valor = input("Ingrese el peso del arma: ")
        arma_detalle = buscar_info_armas('weight', float(valor), categorias)
        if len(arma_detalle) == 0:
            print("No se encontraron armas con ese peso")
        else:
            print("Las armas con peso", valor, "son:")
            for arma in arma_detalle:
                print("-", arma[0], "(", arma[1], ")")
        menu_busqueda_armas(categorias)

    elif opcion == '4':
        print("Adios")
        return

    else:
        print("Opcioin invalida, por favor intenta de nuevo")
        menu_busqueda_armas(categorias)

def requisitos_armas(categorias):
    streg = int(input("Introduce tu nivel de fuerza: "))
    dex = int(input("Introduce tu nivel de destreza: "))
    intel = int(input("Introduce tu nivel de inteligencia: "))
    faith = int(input("Introduce tu nivel de fe: "))
    armas_disponibles = []
    categorias_disponibles = []
    for categoria in categorias:
        for arma in categoria[list(categoria.keys())[1]]:
            if "requirements" not in arma or (arma["requirements"]["str"] <= streg and arma["requirements"]["dex"] <= dex and arma["requirements"]["int"] <= intel and arma["requirements"]["faith"] <= faith):
                if "name" in arma:
                    armas_disponibles.append(arma["name"])
                    if "category" in categoria:
                        categorias_disponibles.append(categoria["category"])
                    else:
                        print("No se encontró el nombre de una categoría en una categoría.")
                else:
                    print("No se encontró el nombre de un arma en la categoría.")
    print("Puedes utilizar", len(armas_disponibles), "armas:")
    for nombre_arma in armas_disponibles:
        print(nombre_arma)
    categorias_disponibles = set(categorias_disponibles)
    print("Puedes utilizar", len(categorias_disponibles), "categorías:")
    for categoria in categorias_disponibles:
        print(categoria)
    for categoria in categorias:
        nombre_categoria = next(iter(categoria))
        armas_categoria = categoria[nombre_categoria]
        cantidad_armas_disponibles = len([arma for arma in armas_categoria if "requirements" not in arma or (arma["requirements"]["str"] <= streg and arma["requirements"]["dex"] <= dex and arma["requirements"]["int"] <= intel and arma["requirements"]["faith"] <= faith)])
        print("En la categoria", nombre_categoria, "hay", cantidad_armas_disponibles, "armas.")










