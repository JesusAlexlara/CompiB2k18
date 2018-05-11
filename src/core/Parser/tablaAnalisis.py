import codecs

tablaSL = [
    '}', 'C', 'r', 'e', 'a', 'V', 'n', 't', '(', 'i', 'd', ',', 'u', 'm', ')', ';', 'L', 'b', 'l', 'B', 'o', 'T',
    'x', 'E', 'v', 'M', '{', 'f', 's', 'p', ':', '=', 'w', 'h', 'c', 'k', 'I', '>', '<', '!', '+', '-', 'g', '^', '*',
    '/', '$', 'programa', 'estructura', 'def', 'def-func', 'def-vent', 'def-ctrl', 'crea-control', 'def-evnt',
    'def-main', 'secuencia-sent', 'sentencia', 'sent-if', 'sent-repeat', 'sent-assign', 'sent-while', 'sent-switch',
    'secuencia-case', 'sentencia-case', 'sentencia-default', 'sent-for', 'sent-func', 'sent-declara', 'identificadores',
    'exp', 'op-comparacion', 'exp-simple', 'opsuma', 'tipo', 'term', 'potencia', 'opmult', 'factor', 'const'
]

def genera_tabla():
    tabla = []
    with open('./core/Parser/tablaAcc.t') as f:
        content = f.readlines()
    for renglon in content:
        campos = renglon.strip().split(" ")
        tam = len(campos)
        diccionario = {}
        contador = 0
        for cadena in campos:
            identificador = tablaSL[contador]
            diccionario.update({identificador: cadena})
            contador = contador + 1
        tabla.append(diccionario)
    return tabla

if __name__ == "__main__":
    tabla = genera_tabla()

    print(tabla[0]['M'])
    print(tabla[105]['}'])
    print(tabla[0]['def'])

