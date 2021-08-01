
from tratamientolistas import *
import os

    elif opc == '3':
        opc1 = ''
        while opc1 != '11':
            os.system("cls")
            menu1 = Menu('//--MENU TRATAMIENTO DE LISTAS--//',
                         ['1) Presentar Lista', '2) BuscarLista', '3) ListaFactorial', '4) ListaPrimo', '5) ListaNotas',
                          '6) InsertarLista', '7) Eliminar Lista', '8) RetornaValorLista', '9) CopiarTuplaLista',
                          '10) VueltoLista', '11) Salir'])
            opc1 = menu1.menu()
            if opc1 == '1':
                def presentarLista(self):
                    for elemento in self.lista:
                        print(elemento)
                        input("Presione una tecla para continuar...")
            if opc1 == '2':
                def buscarLista(self, valor):
                    for elemento in self.lista:
                        if (elemento == valor):
                        print("Se ha encontrado el valor de {} en la lista".format(valor))
                    else:
                        print("No se ha encontrado el valor de {} en la lista".format(valor))
                        input("Presione una tecla para continuar...")
            if opc1 == '3':
                def listaFactorial(self):
                    for i in self.lista:
                        if type(i) == int:
                            print("El factorial del numero {} es {}".format(i, obj.factorial(i)))
                            input("Presione una tecla para continuar...")
            if opc1 == '4':
                def listaPrimo(self):
                    lista = []
                    for elemento in self.lista:
                        if (esPrimo(elemento)):
                            lista.append(elemento)
                    return lista
                    input("Presione una tecla para continuar...")
            if opc1 == '5':
                def listaNotas(self, listaNotasDicccionario):
                    for key in listaNotasDicccionario.keys():
                        print(key)
                        for nota in listaNotasDicccionario[key]:
                            print(nota, end="")
                        print("")
                        input("Presione una tecla para continuar...")
            if opc1 == '6':
                def insertarLista(self, posicion, valor):
                    auxlist = []
                    for i in range(len(self.lista)):
                        if i < posicion:
                            auxlist.append(self.lista[i])
                    auxlist.append(valor)
                    auxlist = auxlist + self.lista[posicion:]
                    return auxlist
                    input("Presione una tecla para continuar")
            if opc1 == '7':
                def eliminarLista(self, valor):
                    for i in self.lista:
                        if i == valor:
                            self.lista.remove(valor)
                    return self.lista
            if opc1 == '8':
                def retornar(self, pos):
                    for posicion, valor in enumerate(self.lista):
                        if pos == posicion:
                            print(valor)
                    self.lista.pop(pos)
                    print(self.lista)
                    input("Presione una tecla para continuar...")
            if opc1 == '9':
                def tuplalista(self, tupla):
                    list = []
                    for i in tupla:
                        list.append(i)
                        input("Presione una tecla para continuar...")
                    return list
            if opc1 == '10':
                def vueltoLista(self, listaClientesDiccionario):
                    for key in listaClientesDiccionario.keys():
                        print(key)
                        tmp = 0
                        for gasto in listaClientesDiccionario[key]:
                            tmp += gasto
                        print(tmp)
                        input("Presione una tecla para continuar...")

os.system("cls")