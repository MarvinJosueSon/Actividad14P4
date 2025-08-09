participanteDic={}

def ingresar():
    try:
        idAux=input("Ingrese el ID de la participante: ")
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
                    categoria=None
                if(categoria != None):
                    participanteDic[idAux]={
                        "nombre":nombreAux,
                        "edad":edadAux,
                        "categoria":categoriaAux
                    }
                    print("INGRESADO CORRECTAMENTE")
                else:
                    print("ERROR: DATOS INGRESADOS NO VALIDOS")
    except ValueError:
        print("ERROR: DATOS INGRESADOS NO VALIDOS")
