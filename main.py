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
    except ValueError:
        print("ERROR: DATOS INGRESADOS NO VALIDOS")

ingresar()
