import sys
import re

RESERVADA = "RESERVADA"
KEYWORD   = "KEYWORD"

COMPARACION = "COMPARACION"
OPSUMA = "OPSUMA"
OPMULT = "OPMULT"
TIPO = "TIPO"
NUM = "NUM"
ID = "ID"

exp_tokens = [
    [r'[ \n\t]+', None, None],
    [r'#[^\n]*', None, None],
    [r'(int?)(?=\s)', 'int', TIPO],
    [r'(float?)(?=\s)', 'float', TIPO],
    [r'(string?)(?=\s)', 'string', TIPO],
    [r'{', '{',RESERVADA],
    [r'}', '}', RESERVADA],
    [r'\(', '(', RESERVADA],
    [r'\)', ')', RESERVADA],
    [r'(for?)(?=\()', 'for', RESERVADA],
    [r'(while?)(?=\()', 'while', RESERVADA],
    [r'(swith?)(?=\()', 'switch', RESERVADA],
    [r'(case?)(?=\s)', 'case', RESERVADA],
    [r'(break?)(?=;)', 'break', RESERVADA],
    [r'(def?)(?=\s)', 'def', RESERVADA],
    [r'(CreaVentana?)(?=\()', 'CreaVentana', RESERVADA],
    [r'(?:[0-9]+(?:\.[0-9]*)?|(?:[0-9]+)?\.[0-9]+)', 'num', NUM],
    [r',', ',', RESERVADA],
    [r'(CreaLabel?)(?=\()', 'CreaLabel', RESERVADA],
    [r'(CreaBoton?)(?=\()', 'CreaBoton', RESERVADA],
    [r'(CreaEvento?)(?=\()', 'CreaEvento', RESERVADA],
    [r'(CreaTextbox?)(?=\()', 'CreaTextbox', RESERVADA],
    [r'\b(Main?)\b', 'Main', RESERVADA],
    [r'(if?)(?=\()', 'if', RESERVADA],
    [r'(else?)(?={)', 'else', RESERVADA],
    [r'(repeat?)(?={)', 'repeat', RESERVADA],
    [r'(until?)(?=\()', 'until', RESERVADA],
    [r'\:=', ':=', RESERVADA],
    [r'(default?)(?={)', 'default', RESERVADA],
    [r'(for?)(?=\()', 'for', RESERVADA],
    [r'step', 'step', RESERVADA],
    [r'\:', ':', RESERVADA],
    [r'(CierraVentana?)(?=\()', 'CierraVentana', RESERVADA],
    [r'(LeeTextBox?)(?=\()', 'LeeTextBox', RESERVADA],
    [r'(Loop?)(?=\()', 'Loop', RESERVADA],
    [r'(ImprimeTextBox?)(?=\()', 'ImprimeTextBox', RESERVADA],
    [r'(Concat?)(?=\()', 'Concat', RESERVADA],
    [r'(Mbox?)(?=\()', 'Mbox', RESERVADA],
    [r'==', '==', COMPARACION],
    [r'>=', '>=', COMPARACION],
    [r'<=', '<=', COMPARACION],
    [r'!=', '!=', COMPARACION],
    [r'\+', '+', OPSUMA],
    [r'-', '-', OPSUMA],
    [r'\^', '^', RESERVADA],
    [r'=', '=', RESERVADA],
    [r';', ';', RESERVADA],
    [r'(vent?)(?=\s)', 'vent', RESERVADA],
    [r'(textBox?)(?=\s)', 'textBox', RESERVADA],
    [r'(label?)(?=\s)', 'label', RESERVADA],
    [r'(boton?)(?=\s)', 'boton', RESERVADA],
    [r'\*', '*', OPMULT],
    [r'/', '/', OPMULT],
    [r'>', '>', COMPARACION],
    [r'<', '<', COMPARACION],
    [r'\"(.*?)\"', 'id', ID],
    [r'[A-Za-z][A-Za-z0-9_]*', 'id', ID],
]


def lex(cadena):
    return lexer(cadena, exp_tokens)


def lexer(cadena, exp_tokens):
    tokens = []
    pos = 0
    while pos < len(cadena):
        res = None
        for expt in exp_tokens:
            expresion, etiq, tipo = expt
            rex = re.compile(expresion)
            res = rex.match(cadena, pos)
            if res:
                text = res.group(0)
                if tipo:
                    token = (etiq, text, tipo)
                    tokens.append(token)
                break
        if not res:
            sys.stderr.write('Caracter invalir: %s\n' % cadena[pos])
            break
        else:
            pos = res.end(0)
    return tokens


