participanteDic={}

def ingresar():
    try:
        cantidad=int(input("Ingrese la cantidad de participantes a agregar: "))
        if cantidad>0 :
            i=1
            while i<=cantidad:

                idAux=input(f"Ingrese el ID de la participante #{i}: ")
                if not idAux in participanteDic:
                    nombreAux=input("Ingrese el nombre: ")
                    edadAux=int(input("Ingrese la edad: "))
                    if edadAux>17:
                        print("Categorias disponibles: 1.Juvenil; 2.Master; 3.Adulto")
                        cat=input("Ingrese el numero de  categoria: ")
                        if cat=="1":
                            categoriaAux="Juvenil"
                        elif cat=="2":
                            categoriaAux="Master"
                        elif cat=="3":
                            categoriaAux="Adulto"
                        else:
                            print("Categoria incorrecta")
                            categoria=""
                        if(categoriaAux !=""):
                            participanteDic[idAux]={
                                "nombre":nombreAux,
                                "edad":edadAux,
                                "categoria":categoriaAux
                            }
                            i=i+1
                            print("INGRESADO CORRECTAMENTE")
                        else:
                            print("ERROR: DATOS INGRESADOS NO VALIDOS")
                else:
                    print("ID YA EXISTENTE")
    except ValueError:
        print("ERROR: DATOS INGRESADOS NO VALIDOS")

def quicksort(lista, clave):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[clave] <= pivote[clave]]
        mayores = [x for x in lista[1:] if x[clave] > pivote[clave]]
        return quicksort(menores, clave) + [pivote] + quicksort(mayores, clave)

def mostrar_ordenados_nombre():
    participantes_lista = list(participanteDic.values())
    ordenados = quicksort(participantes_lista, "nombre")
    print("--- Participantes ordenados por nombre ---")
    for p in ordenados:
        print(f"{p['nombre']} - Edad: {p['edad']} - Categoría: {p['categoria']}")

def mostrar_ordenados_edad():
    participantes_lista = list(participanteDic.values())
    ordenados = quicksort(participantes_lista, "edad")
    print("\n--- Participantes ordenados por edad ---")
    for p in ordenados:
        print(f"{p['nombre']} - Edad: {p['edad']} - Categoría: {p['categoria']}")

while True:
    print("===MENU===")
    print("1. Ingresar participantes")
    print("2. Ver ordenados por nombre")
    print("3. Ver ordenados por edad")
    print("4. Salir")
    opcion=input("Ingrese el numero de opcion: ")
    match opcion:
        case "1":
            ingresar()
        case "2":
            mostrar_ordenados_nombre()
        case "3":
            mostrar_ordenados_edad()
        case "4":
            print("Saliendo...")
            break
