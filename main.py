import pickle
import os
import threading

def revisar(dato):
    global guardar
    while bandera == True:
        if guardar == True:
            respaldo = open('respaldo.pickle', 'wb')
            pickle.dump(dato, respaldo)
            respaldo.close()
            guardar = False


print("AGENDA TELEFONICA")
contactos = []

if os.path.exists('datos.pickle'):
    archivo = open('datos.pickle', 'rb')
    while True:
        try:
            contactos.append(pickle.load(archivo))
        except EOFError:
            break
    archivo.close()

while True:
    print("\nEscoge una opcion:")
    print("1) Agregar contacto")
    print("2) Mostrar contactos")
    print("3) Buscar contacto")
    print("4) Borrar todo")
    print("5) Salir")
    opcion = input("> ")

    if opcion == "1":
        contacto = dict()

        if os.path.exists('respaldo.pickle'):
            restaurar = open('respaldo.pickle', 'rb')
            contacto = pickle.load(restaurar)
            restaurar.close()

        bandera = True
        guardar = False

        hilo1 = threading.Thread(target=revisar, args=(contacto,))
        hilo1.start()

        if 'Nombre' in contacto:
            print("Introduce el nombre del contacto: " + contacto['Nombre'])
        else:
            nombre = input("Introduce el nombre del contacto: ")
            contacto['Nombre'] = nombre
            guardar = True
        
        if 'Telefono' in contacto:
            print("Introduce su telefono: " + contacto['Telefono'])
        else:
            while True:
                telefono = (input("Introduce su telefono: "))
                try:
                    n = int(telefono)
                    contacto['Telefono'] = telefono
                    guardar = True
                    break 
                except ValueError:
                    print("Solo debe contener numeros.\n")

        while True:
            correo = input("Introduce su correo: ")
            if '@' in correo and correo.rfind('@') != 0:
                contacto['Correo'] = correo
                break
            else:
                print("Correo no valido.\n")
            
        bandera = False
        os.remove("respaldo.pickle")

        contactos.append(contacto)
        archivo = open('datos.pickle', 'ab')
        pickle.dump(contacto, archivo)
        archivo.close()

    elif opcion == "2":
        if len(contactos) == 0:
            print("No hay contactos.")
        else:
            for contacto in contactos:
                print('\n'.join("{}: {}".format(k, v) for k, v in contacto.items()) + '\n')
        
    elif opcion == "3":
        busqueda = input("Introduce el nombre del contacto: ")
        encontrado = False
        for contacto in contactos:
            if contacto['Nombre'] == busqueda:
                encontrado = True
                print('\n'.join("{}: {}".format(k, v) for k, v in contacto.items()))
                break
        if encontrado == False:
            print("No se encuentra este contacto.")

    elif opcion == "4":
        if len(contactos) != 0:
            contactos.clear()
            os.remove("datos.pickle")
            print("Contactos eliminados con exito.")
        else:
            print("No hay contactos.")

    elif opcion == "5":
        print("Hasta luego.\n")
        break

    else:
        print("Opcion no valida.")