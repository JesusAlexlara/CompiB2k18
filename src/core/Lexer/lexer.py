import sys
import re

RESERVADA = "RESERVADA"
KEYWORD   = "KEYWORD"
STRING    = "STRING"

exp_tokens = [
    [r'[ \n\t]+', None, None],
    [r'#[^\n]*', None, None],
    [r'(int?)(?=\s)', 'int', KEYWORD],
    [r'(float?)(?=\s)', 'float', KEYWORD],
    [r'(string?)(?=\s)', 'string', KEYWORD],
    [r';', ';', RESERVADA],
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
    [r'[+-]?[0-9]+(.[0-9])+?', 'num', KEYWORD],
    [r',', ',', RESERVADA],
    [r'(CreaLabel?)(?=\()', 'CreaLabel', RESERVADA],
    [r'(CreaBoton?)(?=\()', 'CreaBoton', RESERVADA],
    [r'(CreaEvento?)(?=\()', 'CreaEvento', RESERVADA],
    [r'(Main?)(?=\()', 'Main', RESERVADA],
    [r'(if?)(?=\()', 'if', RESERVADA],
    [r'(else?)(?={)', 'else', RESERVADA],
    [r'(repeat?)(?={)', 'repeat', RESERVADA],
    [r'(until?)(?=\()', 'until', RESERVADA],
    [r'\:=', ':=', RESERVADA],
    [r'(default?)(?={)', 'default', RESERVADA],
    [r'(for?)(?=\()', 'for', RESERVADA],
    [r'=', '=', RESERVADA],
    [r'step', 'step', RESERVADA],
    [r'\:', ':', RESERVADA],
    [r'(CierraVentana?)(?=\()', 'CierraVentana', RESERVADA],
    [r'(LeeTextBox?)(?=\()', 'LeeTextBox', RESERVADA],
    [r'(Loop?)(?=\()', 'Loop', RESERVADA],
    [r'(ImprimeTextBox?)(?=\()', 'ImprimeTextBox', RESERVADA],
    [r'(Concat?)(?=\()', 'Concat', RESERVADA],
    [r'(Mbox?)(?=\()', 'Mbox', RESERVADA],
    [r'==', '==', RESERVADA],
    [r'>=', '>=', RESERVADA],
    [r'<=', '<=', RESERVADA],
    [r'!=', '!=', RESERVADA],
    [r'\+', '+', RESERVADA],
    [r'-', '-', RESERVADA],
    [r'(vent?)(?=\s)', 'vent', RESERVADA],
    [r'(textBox?)(?=\s)', 'textBox', RESERVADA],
    [r'(label?)(?=\s)', 'label', RESERVADA],
    [r'(boton?)(?=\s)', 'boton', RESERVADA],
    [r'\*', '*', RESERVADA],
    [r'/', '/', RESERVADA],
    [r'>', '>', RESERVADA],
    [r'<', '<', RESERVADA],
    [r'\"(.*?)\"', 'id', STRING],
    [r'[A-Za-z][A-Za-z0-9_-]*', 'id', KEYWORD],
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


