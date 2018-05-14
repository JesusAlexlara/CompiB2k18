'''
programa-><estructura><def-main>
programa-><def-main>
estructura-><estructura><def>
estructura-><def>
def-><sent-declara>
def-><def-func>
def-func->defid{<secuencia-sent>}
def-vent->CreaVentana(id,id,num,num,num,num);
def-ctrl-><crea-control>
def-ctrl->CreaLabel(id,id,num,num,id);
crea-control->CreaBoton(id,id,id,num,num,num,num);
crea-control->CreaTextbox(id,id,num,num,num,num);
def-evnt->CreaEvento(id,id);
def-main->Main{<secuencia-sent>}
secuencia-sent-><secuencia-sent><sentencia>
secuencia-sent-><sentencia>
sentencia-><sent-if>
sentencia-><sent-repeat>
sentencia-><sent-assign>
sentencia-><sent-while>
sentencia-><sent-switch>
sentencia-><sent-for>
sentencia-><sent-func>
sentencia-><def-vent>
sentencia-><def-ctrl>
sentencia-><def-evnt>
sentencia-><sent-declara>

sent-if->if(<exp>){<secuencia-sent>}
sent-if->if(<exp>){<secuencia-sent>}else{<secuencia-sent>}
sent-repeat->repeat{<secuencia-sent>}until(<exp>)
sent-assign->id:=<exp>;

sent-while->while(<exp>){<secuencia-sent>}
sent-switch->switch(id){<secuencia-case>}
secuencia-case-><secuencia-case><sentencia-case>
secuencia-case-><sentencia-case>
sentencia-case->case<const>{<secuencia-sent>}break;

sentencia-default->default{<secuencia-sent>}break;
sent-for->for(id=const:const,stepnum){<secuencia-sent>}
sent-func->id();
sent-func->CierraVentana(id);
sent-func->LeeTextBox(id,id);
sent-func->l
sent-func->ImprimeTextBox(id,id);
sent-func->Concat(id,id);
sent-func->Mbox(id);
sent-declara-><tipo><identificadores>;
identificadores-><identificadores>,id
identificadores->id
exp-><exp-simple><op-comparacion><exp-simple>
exp-><exp-simple>
op-comparacion->==
op-comparacion->ɣ
op-comparacion->ɢ
op-comparacion->ɣ=
op-comparacion->ɢ=
op-comparacion->!=
exp-simple-><exp-simple><opsuma><term>
exp-simple-><term>
opsuma->+
opsuma->-
tipo->int
tipo->float
tipo->string
tipo->vent
tipo->textBox
tipo->label
tipo->boton
term-><term><opmult><potencia>
term-><potencia>
potencia-><potencia>^<factor>
potencia-><factor>
opmult->*
opmult->/
factor->(<exp>)
factor->num
factor->id
const->num
const->id
'''

from functools import reduce
import operator

gramatica = [
    ['programa\'', 'programa'],
    ['programa', 'estructura', 'def-main'],
    ['programa', 'def-main'],
    ['estructura', 'estructura', 'def'],
    ['estructura', 'def'],
    ['def', 'sent-declara'],
    ['def', 'def-func'],
    ['def-func', 'd','e','f','i','d','{', 'secuencia-sent', '}'],
    ['def-vent', 'C', 'r', 'e', 'a', 'V', 'e', 'n', 't', 'a', 'n', 'a', '(', 'i', 'd', ',', 'i', 'd', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ')', ';'],
    ['def-ctrl', 'crea-control'],
    ['def-ctrl', 'C', 'r', 'e', 'a', 'L', 'a', 'b', 'e', 'l', '(', 'i', 'd', ',', 'i', 'd', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ',', 'i', 'd', ')', ';'],
    ['crea-control', 'C', 'r', 'e', 'a', 'B', 'o', 't', 'o', 'n', '(', 'i', 'd', ',', 'i', 'd', ',', 'i', 'd', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ')', ';'],
    ['crea-control', 'C', 'r', 'e', 'a', 'T', 'e', 'x', 't', 'b', 'o', 'x', '(', 'i', 'd', ',', 'i', 'd', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ',', 'n', 'u', 'm', ')', ';'],
    ['def-evnt', 'C', 'r', 'e', 'a', 'E', 'v', 'e', 'n', 't', 'o', '(', 'i', 'd', ',', 'i', 'd', ')', ';'],
    ['def-main', 'M', 'a', 'i', 'n', '{', 'secuencia-sent', '}'],
    ['secuencia-sent','secuencia-sent', 'sentencia'],
    ['secuencia-sent', 'sentencia'],
    ['sentencia','sent-if'],
    ['sentencia','sent-repeat'],
    ['sentencia','sent-assign'],
    ['sentencia','sent-while'],
    ['sentencia','sent-switch'],
    ['sentencia','sent-for'],
    ['sentencia','sent-func'],
    ['sentencia','def-vent'],
    ['sentencia','def-ctrl'],
    ['sentencia','def-evnt'],
    ['sentencia','sent-declara'],
    ['sent-if', 'i', 'f', '(', 'exp', '{', 'secuencia-sent', '}'],
    ['sent-if', 'i', 'f', '(', 'exp', '{', 'secuencia-sent', '}', 'e', 'l', 's', 'e', '{', 'secuencia-sent', '}'],
    ['sent-repeat', 'r', 'e', 'p', 'e', 'a', 't', '{', 'secuencia-sent', '}', 'u', 'n', 't', 'i', 'l', '(', 'exp', ')'],
    ['sent-assign', 'i', 'd', ':', '=', 'exp', ';'],
    ['sent-while', 'w', 'h', 'i', 'l', 'e', '(', 'exp', ')', '{', 'secuencia-sent', '}'],
    ['sent-switch', 's', 'w', 'i', 't', 'c', 'h', '(', 'i', 'd', ')', '{', 'secuencia-case', '}'],
    ['secuencia-case', 'secuencia-case', 'sentencia-case'],
    ['secuencia-case', 'sentencia-case'],
    ['sentencia-case', 'c', 'a', 's', 'e', 'const', '{', 'secuencia-sent', '}', 'b', 'r', 'e', 'a', 'k', ';'],
    ['sentencia-default', 'd', 'e', 'f', 'a', 'u', 'l', 't', '{', 'secuencia-sent', '}', 'b', 'r', 'e', 'a', 'k', ';'],
    ['sent-for', 'f', 'o', 'r', '(', 'i', 'd', '=', 'c', 'o', 'n', 's', 't', ':', 'c', 'o', 'n', 's', 't', ',', 's', 't', 'e', 'p', 'n', 'u', 'm', ')', '{', 'secuencia-sen','}'],
    ['sent-func','i', 'd', '(', ')', ';'],
    ['sent-func','C', 'i', 'e', 'r', 'r', 'a', 'V', 'e', 'n', 't', 'a', 'n', 'a', '(', 'i', 'd', ')', ';'],
    ['sent-func','L', 'e', 'e', 'T', 'e', 'x', 't', 'B', 'o', 'x', '(', 'i', 'd', ',', 'i', 'd', ')', ';'],
    ['sent-func', 'L', 'o', 'o', 'p', '(', 'i', 'd', ')', ';'],
    ['sent-func','I', 'm', 'p', 'r', 'i', 'm', 'e', 'T', 'e', 'x', 't', 'B', 'o', 'x', '(', 'i', 'd', ',', 'i', 'd', ')', ';'],
    ['sent-func','C', 'o', 'n', 'c', 'a', 't', '(', 'i', 'd', ',', 'i', 'd', ')', ';'],
    ['sent-func','M', 'b', 'o', 'x', '(', 'i', 'd', ')', ';'],
    ['sent-declara', 'tipo', 'identificadores', ';'],
    ['identificadores', 'identificadores', ',', 'i', 'd'],
    ['identificadores', 'i', 'd'],
    ['exp', 'exp-simple', 'op-comparacion','exp-simple'],
    ['exp', 'exp-simple'],
    ['op-comparacion','=', '='],
    ['op-comparacion','>'],
    ['op-comparacion','<'],
    ['op-comparacion','>', '='],
    ['op-comparacion','<', '='],
    ['op-comparacion','!', '='],
    ['exp-simple', 'exp-simple','opsuma', 'term'],
    ['exp-simple', 'term'],
    ['opsuma', '+'],
    ['opsuma', '-'],
    ['tipo','i', 'n', 't'],
    ['tipo','f', 'l', 'o', 'a', 't'],
    ['tipo','s', 't', 'r', 'i', 'n', 'g'],
    ['tipo','v', 'e', 'n', 't'],
    ['tipo','t', 'e', 'x', 't', 'B', 'o', 'x'],
    ['tipo','l', 'a', 'b', 'e', 'l'],
    ['tipo','b', 'o', 't', 'o', 'n'],
    ['term', 'term', 'opmult', 'potencia'],
    ['term', 'potencia'],
    ['potencia', 'potencia', '^', 'factor'],
    ['potencia', 'factor'],
    ['opmult', '*'],
    ['opmult', '/'],
    ['factor', '(', 'exp',')'],
    ['factor', 'n', 'u', 'm'],
    ['factor', 'i', 'd'],
    ['const', 'n', 'u', 'm'],
    ['const', 'i', 'd'],
]


def carga_gramatica():
    g = []
    with open('gramatica.txt', 'r') as gramatica:
        for r in gramatica.readlines():
            cut = r.split('->')
            produccion = []
            produccion.append(cut[0].replace(' ', ''))
            cut = cut[1].split(' ')

            for t in cut:
                if t:
                    produccion.append(t.replace(' ', ''))
            g.append(produccion)
    return g

def str_gram(p):
    std = ''
    for n in gramatica[p][1:]:
        std = std + ' ' + n
    return '( ' + str(gramatica[p][0]) + str(' -> ') + std + ' )'




if __name__ == "__main__":
    gramatica = carga_gramatica()
    print(gramatica)



