import os
import time
import random
listaMascotas = []


def limpiar():
    os.system("cls")

def menu():
    print("1. Grabar/Registrar Mascota")
    print("2. Listar Todos los registros")
    print("3. Buscar Mascota")
    print("4. Imprimir Reportes por tipo mascota")
    print("")
    print("5. Cerrar programa.")

def registrar():
    i = True
    while i == True:
        idMascota = (input("Ingrese ID mascota:\n"))
        if len(idMascota) > 0 and len(idMascota) == 5:
            print("ID ingresado valido.")
            time.sleep(2)
            limpiar()
            i = False
        else:
            print("ID ingresado invalido.")
            time.sleep(2)
    i = True
    while i == True:
        nombre = input("Ingrese nombre de la mascota:\n")
        if len(nombre) > 0:
            print("Nombre ingresado correctamente.")
            time.sleep(2)
            limpiar()
            i = False
        else:
            print("Nombre ingresado debe tener al menos un caracter.")
            time.sleep(2)
            limpiar()
    i = True
    while i == True:
        nombreDueño = input("Ingrese nombre del dueño:\n")
        if len(nombreDueño) > 0:
            print("Nombre ingresado valido.")
            time.sleep(2)
            limpiar()
            i = False
        else:
            print("Nombre ingresado debe tener al menos un caracter.")
            time.sleep(2)
            limpiar()
    tipo = input("Seleccione un numero:\n1. Perro\n2. Gato\n")
    if tipo != "1" and tipo != "2":
        print("Escriba una opción disponible por favor.")
    else:
        if tipo == "1":
            print("tipo seleccionado: Perro")
            time.sleep(2)
            limpiar()
            tipo = "Perro"
        else:
            tipo = "Gato"
            print("Tipo seleccionado: Gato")
            time.sleep(2)
            limpiar()
    mascota = {"id":idMascota,"nombre":nombre,"nombreDueño":nombreDueño,"tipo":tipo}
    listaMascotas.append(mascota)

def listar():
    if len(listaMascotas) == 0:
        print("No se ha registrado nada aún. Por favor, ingrese una mascota para poder mostrar la lista.")
    else:
        for mascota in listaMascotas:
            print(f"ID: {mascota['id']} Nombre: {mascota['nombre']} Nombre dueño: {mascota['nombreDueño']} Tipo: {mascota['tipo']}")
            print("")

def buscarMascota(id):
    encontrado = False
    for mascota in listaMascotas:
        if mascota['id']== str(id):
            print(f"ID: {mascota['id']} Nombre: {mascota['nombre']} Nombre dueño: {mascota['nombreDueño']} Tipo: {mascota['tipo']}")
            print("")
            encontrado = True
            
        else:
            print("No existe ese Registro")

def reporte():
    tipo = input("Ingresar tipo de mascota, (Perro o Gato):\n")
    encontrado = False
    for mascota in listaMascotas:
        if mascota['tipo'].lower()== tipo.lower():
            vacunas = random.randint(1, 10)
            print(f"ID: {mascota['id']} Nombre: {mascota['nombre']} Dueño de la mascota: {mascota['nombreDueño']} Tipo: {mascota['tipo']} Vacunas faltantes: {vacunas}")
            print("")
            encontrado = True
        else:
            print("No existe ese Registro")

def cerrar():
    limpiar()
    print("Programa cerrado.")

while True:
    
    menu()
    op=int(input("Seleccione una opción:\n"))
    if op==1:
        
        print("Seleccionaste la opción:\nGrabar/Registrar Mascota")
        registrar()
    if op==2:
        
        print("2. Seleccionaste la opción:\nListar Todos los registros")
        listar()
    if op==3:
        
        print("Seleccionaste la opción:\nBuscar Mascota")
        if len(listaMascotas) == 0:
            print("No se ha registrado nada aún. Por favor, ingrese una mascota para poder buscar.")
        else:
            id = int(input("Ingrese el ID de la mascota que busca por favor:\n"))
            buscarMascota(id)
    if op==4:
        reporte()
    if op==5:
        limpiar()
        cerrar()
        break

