import PyQt5.QtWidgets
import PyQt5.Qsci
import sys
import re


class LexerTiny(PyQt5.Qsci.QsciLexerCustom):
    styles = {
        "Default": 0,
        "Keyword": 1,
        "Unsafe": 2,
        "MultilineComment": 3,
    }

    keyword_list = [
       'CreaVentana', 'CreaLabel', 'CreaBoton', 'CreaTextbox', 'CreaEvento', 'Main', 'if',
        'else', 'repeat', 'until', ':=', 'while', 'swich', 'case', 'break', 'deafult',
        'for', 'CierraVentana', 'LeeTextBox', 'Loop', 'ImprimeTextBox', 'Concat', 'Mbox', 'def', 'loop'

    ]
    unsafe_keyword_list = [
        "int", "float", "string", "vent", "textBox", "label",
        "boton", "label"
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        # Set the default style values
        self.setDefaultColor(PyQt5.QtGui.QColor(0x00, 0x00, 0x00))
        self.setDefaultPaper(PyQt5.QtGui.QColor(0xff, 0xff, 0xff))
        self.setDefaultFont(PyQt5.QtGui.QFont("Source Code Pro", 18))
        # Initialize all style colors
        self.init_colors()
        # Init the fonts
        for i in range(len(self.styles)):
            if i == self.styles["Keyword"]:
                self.setFont(PyQt5.QtGui.QFont("Source Code Pro", 18,
                                               weight=PyQt5.QtGui.QFont.Black), i)
        else:
            self.setFont(PyQt5.QtGui.QFont("Source Code Pro", 18), i)

    def init_colors(self):
            # Font color
            self.setColor(PyQt5.QtGui.QColor(0x00, 0x00, 0x00),
                          self.styles["Default"])
            self.setColor(PyQt5.QtGui.QColor(0x00, 0x00, 0x7f),
                          self.styles["Keyword"])
            self.setColor(PyQt5.QtGui.QColor(0x7f, 0x00, 0x00),
                          self.styles["Unsafe"])
            self.setColor(PyQt5.QtGui.QColor(0x7f, 0x7f, 0x00),
                          self.styles["MultilineComment"])
            # Paper color
            for i in range(len(self.styles)):
                self.setPaper(PyQt5.QtGui.QColor(0xff, 0xff, 0xff), i)

                def language(self):

                    return "Nim"

    def description(self, style):
        if style < len(self.styles):
            description = "Custom lexer for the Nim programming languages"
        else:
            description = ""
        return description

    def styleText(self, start, end):
            self.startStyling(start)
        # Tokenize the text that needs to be styled using regular
        # to figure out which style the sequence belongs to.
        # THE PROCEDURE SHOWN BELOW IS JUST ONE OF MANY!
            str_re = r"({\.|\.\}|\#|\'|\"\"\"|\n|\s+|\w+|\W)"
            splitter = re.compile(str_re)
        # Scintilla works with bytes, so we have to adjust the
            text = self.parent().text()[start:end]
            tokens = [(token, len(bytearray(token, "utf-8"))) for token in splitter.findall(text)]
        # Style the text in a loop
            for i, token in enumerate(tokens):
                if token[0] in self.keyword_list:
                    self.setStyling(token[1], self.styles["Keyword"])
                elif token[0] in self.unsafe_keyword_list:
                    self.setStyling(token[1], self.styles["Unsafe"])
                else:
                    self.setStyling(token[1], self.styles["Default"])