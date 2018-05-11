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
sent-func->Loop(id);
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


gramatica = [
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
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]












