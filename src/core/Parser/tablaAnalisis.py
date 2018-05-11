import codecs

tablaSL = [
    '}', 'C', 'r', 'e', 'a', 'V', 'n', 't', '(', 'i', 'd', ',', 'u', 'm', ')', ';', 'L', 'b', 'l', 'B', 'o', 'T',
    'x', 'E', 'v', 'M', '{', 'f', 's', 'p', ':', '=', 'w', 'h', 'c', 'k', 'I', '>', '<', '!', '+', '-', 'g', '^', '*',
    '/', '$', 'programa estructura', 'def', 'def-func', 'def-vent', 'def-ctrl', 'crea-control', 'def-evnt',
    'def-main', 'secuencia-sent', 'sentencia', 'sent-if', 'sent-repeat', 'sent-assign', 'sent-while', 'sent-switch',
    'secuencia-case', 'sentencia-case', 'sentencia-default', 'sent-for', 'sent-func', 'sent-declara', 'identificadores',
    'exp', 'op-comparacion', 'exp-simple', 'opsuma', 'tipo', 'term', 'potencia', 'opmult', 'factor', 'const'
]

def genera_tabla():
    tabla = []
    archivo = codecs.open('./tablaAS.csv', 'r','utf-8')
    try:
        for renglon in archivo.readlines():
            campos = renglon.strip().split(",")
            diccionario = {}
            contador = 0
            for cadena in campos:
                if cadena:
                    identificador = tablaSL[contador]
                    diccionario.update({identificador: cadena})
                contador = contador + 1
            tabla.append(diccionario)
    finally:
        archivo.close()
    return tabla

if __name__ == "__main__":
    genera_tabla()

