from functools import reduce

from .tablaAnalisis import genera_tabla
from .gramatica import *
from ..Utils.grammar import Grammar
from ..Utils.actionTable import ActionTable
from ..Utils.stack import Stack
from ..Utils.program import Program
import operator

class Pila():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items is []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    @property
    def str(self):
        t = len(self.items) - 1
        return reduce(operator.add, self.items[0:t])

    @property
    def str_full(self):
        return reduce(operator.add, self.items)


class Evalua_cadena:
    def __init__(self, cadena):
        self.cadena = cadena + '$'
        self.tabla_as = genera_tabla()
        self.gramatica = gramatica
        self.tabla_ac = []
        self.lista_r = []
        self.variables = []

    def evalua(self):
        if self.cadena and self.tabla_as and self.gramatica:
            stack = '$0'
            tam_remover = 0
            pila = Pila()
            ir_a = False
            old_t = 0
            s = 0
            t = 0
            i = 0
            pila.push(t)
            while i < len(self.cadena):
                accion = []
                c = self.cadena[i]
                s = pila.peek()
                try:
                    res = self.tabla_as[s][c]
                except: return False
                if 'd' in res:
                    t = int(res[1:])
                    stack = stack + c + str(t)
                    tam_remover = len(str(t)) + 1
                    pila.push(t)
                    #elementos
                    accion.append(stack)
                    accion.append(self.cadena[i+1:])
                    accion.append(res)
                    accion.append('')
                    old_t = t
                elif 'r' in res:
                    ir_a = True
                    t = t2 = int(res[1:])
                    elementos = self.gramatica[t]
                    self.lista_r.append(elementos)
                    for xx in range(len(elementos[1:])):
                        pila.pop()
                    t = pila.peek()
                    res = self.tabla_as[t][elementos[0]]
                    if not res.isdigit():
                        return False
                    pila.push(int(res))
                    tam = len(stack) - tam_remover
                    new_stack = stack[:tam*-1]
                    #stack = stack[:tam]
                    stack = new_stack
                    tam_remover = len(elementos[0])
                    accion.append(stack)
                    accion.append(self.cadena[i:])
                    a = ' '
                    accion.append('r' + str(t2) + '= ' + elementos[0] + a.join(elementos[1:]))
                    i = i - 1
                    stack = stack + elementos[0] + res
                    tam_remover = tam_remover + len(res)

                    #Crea arboles o variables



                if res == 'acc':
                    accion.append(stack)
                    accion.append(self.cadena[i + 1:])
                    accion.append(res)
                    accion.append('')
                    self.tabla_ac.append(accion)
                    return True
                self.tabla_ac.append(accion)
                i = i + 1

        else:
            return False


    def pos_gramatica(self, pos):
        cont = 0
        for elemento in self.gramatica:
            for produccion in elemento:
                if cont >= pos:
                    return (elemento, produccion)
                else:
                    cont = cont + 1


class Parser:
    def __init__(self):
        self.tabla_as = ActionTable()
        self.gramatica = Grammar()
        self.tabla_ac = []

        #self.pg = Program()

        self.var_tipo = None
        self.var_id = Stack()
        self.variables = {}



    def evalua(self, tokens):
        self.tabla_as.load('core/Utils/tbAs.csv')
        self.gramatica.load('core/Utils/gramaticav2.txt')

        stack = Stack()
        pila = Stack()

        stack.push('$0')
        pila.push(0)
        edo = 0
        i = 0
        tokens.append(('$', '$', 'FINAL'))

        while i < len(tokens):
            accion = []
            c = tokens[i][0]
            edo = pila.peek()
            res = self.tabla_as.elements[edo][c]


            if 's' in res:
                edo_r = int(res[1:])
                if edo_r == 55:
                    print("Aqui")
                stack.push(c + str(edo_r))
                pila.push(edo_r)
                #cad = reduce(operator.add, tokens[i:][0])+'$'
                #cad = ''.join(tokens[i:][0]) + '$'
                cad = ''
                for count in range(i, len(tokens)):
                    s = tokens[count][0]
                    cad = cad + ' ' + s
                accion.append(stack.str)
                accion.append(cad)
                accion.append(res)
                accion.append('')

                #if tokens[i][2] == 'COMPARACION':
                #    self.pg.comp.push(tokens[i][1])
                #elif tokens[i][2] == 'OPSUMA':
                #    self.pg.opsum.push(tokens[i][1])
                #elif tokens[i][2] == 'OPMULT':
                #    self.pg.opmult.push(tokens[i][1])
                #elif tokens[i][2] == 'TIPO':
                #    self.pg.tipo.push(tokens[i][1])
                #elif tokens[i][2] == 'NUM':
                #    self.pg.num.push(tokens[i][1])
                #elif tokens[i][2] == 'ID':
                #    self.pg.id.push(tokens[i][1])

            elif 'r' in res:
                res_b = res
                d = int(res[1:])

                #self.pg.redux.append([d, self.gramatica.productions[d]])

                produccion = self.gramatica.productions[d][0]
                rd = len(self.gramatica.productions[d][1:])

                accion.append(stack.str_full)

                for xx in range(rd):
                    stack.pop()
                    pila.pop()

                edo = pila.peek()
                res = self.tabla_as.elements[edo][produccion]
                if not res.isdigit():
                    return False

                edo_r = int(res)
                stack.push(produccion + str(edo_r))
                pila.push(edo_r)
                #cad = reduce(operator.add, tokens[i:][0]) + '$'
                cad = ''
                for count in range(i, len(tokens)):
                    s = tokens[count][0]
                    cad = cad + ' ' + s
                accion.append(cad)
                accion.append(res_b + ' - ' + self.gramatica.str(d))
                accion.append('')
                i = i - 1

                #########################Acciones de las reducciones####################

                if produccion == 'tipo':
                    self.var_tipo = tokens[i][1]
                if produccion == 'identificadores':
                    self.var_id.push(tokens[i][1])
                if produccion == 'sent-declara':
                    while self.var_id.is_empty():
                        self.variables[self.var_id.pop()] = [self.var_tipo, None]



            elif res == 'acc':
                return True
            else:
                return False
            self.tabla_ac.append(accion)
            i = i + 1
