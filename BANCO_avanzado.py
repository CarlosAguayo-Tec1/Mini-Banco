"""
Mejora el cajero

Consulta saldo
Depositar
Retirar
Historial
Salir
"""
historial = []
usuarios = []
opcion_menu = 0
historia = ""

historial.append("Se ingreso al *Menu*\n")

while opcion_menu != 5:
    print("\n----**MENU DE CAJERO**----")
    print("1. Registrar Usuario")
    print("2. Consulta de Saldo")
    print("3. Depositar / Retirar")
    print("4. Historial")
    print("5. Salir")

    opcion_menu = int(input("\nIngrese una opcion: "))

    while opcion_menu < 1 or opcion_menu > 5:
        historial.append("Se ingreso una opcion erronea")
        print(f"\nLa opcion que eligio es erronea: '{opcion_menu}'")
        opcion_menu = int(input("Ingrese una opcion: "))
    
    if opcion_menu == 1:
        historial.append("\nSe ingreso a **Registrar Usuario**")
        print("----**Inicio de Sesion**----")
        print("en caso de salir ponga 's'")
        usuario = input("\nIngrese nombre de usuario: ")

        if usuario == "s":
            historial.append("El usuario decidio salir del registro")
            historial.append("Se regreso a *Menu*\n")
        else:
            existencia_usuario = False
            for busqueda_usuario in usuarios:
                if busqueda_usuario[0] == usuario:
                    existencia_usuario = True
                    break
            
            while existencia_usuario and usuario != "s":
                historial.append(f"Se intento crear denuevo el usuario: '{usuario}'")
                print(f"\nEl usuario: '{usuario}' ya existe")
                usuario = input("Ingrese otro nombre de usuario: ")

                if usuario == "s":
                    historial.append("El usuario decidio salir tras un nombre repetido")
                    historial.append("Se regreso a *Menu*\n")
                    break
                    
                if usuario != "s":
                    existencia_usuario = False
                    for busqueda_usuario in usuarios:
                        if busqueda_usuario[0] == usuario:
                            existencia_usuario = True
                            break

            if usuario != "s":
                usuarios.append([usuario, 0])
                print(f"\nFelicitaciones: '{usuario}' se creo correctamente")
                historial.append(f"Creacion de nuevo usuario: '{usuario}'")
                historial.append("Se regreso a *Menu*\n")

    elif opcion_menu == 2:
        print("\n----**Consulta de salario**----")
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
            historial.append("Se intento ingresar a **Consulta de Salarios** sin usuarios registrados")
            historial.append("Se regreso a *Menu*\n")
        else:
            usuario = input("Ingrese su usuario: ")
            busqueda_usuario = usuarios[0]
            verificar_salario = False
            historial.append("Se ingreso a **Consulta de Salario**")
            
            for busqueda_usuario in usuarios:
                if busqueda_usuario[0] == usuario:
                    saldo = busqueda_usuario[1]
                    verificar_salario = True
                    break
                    
            if verificar_salario:
                print(f"\nUsuario: '{usuario}' encontrado")
                print(f"Saldo en usuario: ${saldo}")
                historial.append(f"Consulta de Salario de: {usuario} - ${saldo} ")
                historial.append("Se regreso a *Menu*\n")

            else:
                print(f"El usuario: '{usuario}' no existe")
                historial.append(f"Se regreso a *Menu* por inexistencia de usuario: '{usuario}'\n")

    elif opcion_menu == 3:
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
            historial.append("Se intento ingresar a **Depositar / Retirar** sin usuarios registrados")
            historial.append("Se regreso a *Menu*\n")
        else:
            opcion = 0
            historial.append("\nSe ingreso al *Mini-Menu* de **Depositar / Retirar**")

            while opcion != 3:
                print("\n----**Depositar / Retirar**----")
                print("1. Depositar")
                print("2. Retirar")
                print("3. Salir")

                opcion = int(input("\nSeleccione opcion: "))

                while opcion < 1 or opcion > 3:
                    print("\nLa opcion es erronea")
                    opcion = int(input("Seleccione opcion: "))
                
                if opcion == 1:
                    historial.append("Se ingreso a **Depositar**")
                    print("\n---**Depositar**---")
                    usuario = input("Ingrese usuario: ")
                    busqueda_usuario = usuarios[0]
                    verificar_deposito = False
                
                    for busqueda_usuario in usuarios:
                        if busqueda_usuario[0] == usuario:
                            saldo = busqueda_usuario[1]  
                            verificar_deposito = True
                            break
                    
                    if verificar_deposito:
                        print(f"\nUsuario: '{usuario}' fue encontrado")
                        print(f"Saldo acual: ${busqueda_usuario[1]}")
                        historial.append(f"Ingreso el usuario: {usuario} - ${busqueda_usuario[1]}")

                        while True:
                            deposito = float(input("\nCuanto desea depositar: $"))

                            if deposito <= 0:
                                print(f"La cantidada '${deposito}' no es valida")
                                historial.append(f"Intento depositar una cantidad invalida: ${deposito}")
                            elif deposito > 10000:
                                print("Cantidades superiores a $10,000 deben ser en caja")
                                historial.append(f"Supero la cantidad permitida por depositar: ${deposito}")
                            else:
                                busqueda_usuario[1] += deposito
                                print(f"\nDeposito exitoso de ${deposito}")
                                print(f"Saldo actualizado de ${busqueda_usuario[1]} del usuario '{usuario}'")
                                historial.append(f"Deposito exitoso del usuario: {usuario}")
                                historial.append(f"Actualizacion de datos: {usuario} - ${busqueda_usuario[1]}")
                                historial.append("Se regreso a *Mini-Menu*\n")
                                break
                        
                    else:
                        print(f"No se encontro el usuario: '{usuario}'")
                        historial.append(f"Se regreso a *Mini-Menu* por inexistencia de usuario: '{usuario}'\n")

                elif opcion == 2:
                    historial.append("Se ingreso a **Retirar**")
                    print("\n---**Retirar**---")
                    usuario = input("Ingrese usuario: ")
                    busqueda_usuario = usuarios[0]
                    verificar_retiro = False
                
                    for busqueda_usuario in usuarios:
                        if busqueda_usuario[0] == usuario:
                            saldo = busqueda_usuario[1]
                            if saldo == 0:
                                print("Usted no cuenta con saldo para poder retirar")
                                historial.append(f"El usuario: {usuario} intento retirar sin saldo")
                                historial.append("Se regreso a *Mini-Menu*\n")
                                verificar_retiro = None
                                break
                            else:
                                verificar_retiro = True
                                break
                    
                    if verificar_retiro:
                        print(f"\nUsuario: '{usuario}' fue encontrado")
                        print(f"Saldo acual: ${busqueda_usuario[1]}")
                        historial.append(f"Ingreso el usuario: {usuario} - ${busqueda_usuario[1]}")

                        while True:
                            retiro = float(input("\nCuanto desea retirar: $"))
                            
                            if retiro <= 0:
                                print(f"La cantidada '${retiro}' no es valida")
                                historial.append(f"Intento retirar una cantidad invalida: ${retiro}")
                            elif retiro > 10000:
                                print("Cantidades superiores a $10,000 deben ser en caja")
                                historial.append(f"Supero la cantidad permitida por retiro: ${retiro}")
                                historial.append()
                            elif retiro > busqueda_usuario[1]:
                                print("No tiene esa cantidad de saldo")
                                print(f"Escoja una cantidad menor a ${busqueda_usuario[1]}")
                                historial.append(f"Intento retirar una cantidad de saldo inexistente: ${retiro}")
                                historial.append(f"Saldo actual del usuario: {usuario} - ${busqueda_usuario[1]}")
                            else:
                                busqueda_usuario[1] -= retiro
                                print(f"\nRetiro exitoso de ${retiro}")
                                print(f"Saldo actualizado de ${busqueda_usuario[1]} del usuario '{usuario}'")
                                historial.append(f"Retiro exitoso del usuario: {usuario}")
                                historial.append(f"Actualizacion de datos: {usuario} - ${busqueda_usuario[1]}")
                                historial.append("Se regreso a *Mini-Menu*\n")
                                break
                    else:
                        print(f"No se encontro el usuario: '{usuario}'")
                        historial.append(f"Se regreso a *Mini-Menu* por inexistencia de usuario: '{usuario}'\n")

                else:
                    print("\nRegresando al menu principal...")
                    historial.append("Se regreso a *Menu*\n")

    elif opcion_menu == 4:
        historial.append("\nIngreso al **Historial**")
        print("----**Historial de actividades**----\n")
        for historia in historial:
            print(historia)
        historial.append("Se regreso a *Menu*\n")

    else:
        print("Saliendo del programa...")