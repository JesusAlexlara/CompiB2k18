from PyQt5.QtGui import (QFont, QIcon, QKeySequence, QTextCharFormat,
                         QTextCursor, QTextTableFormat)
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDockWidget, QFileDialog,
                             QFileDialog, QListWidget, QMainWindow, QMessageBox, QTextEdit, QTableWidget,
                             QTableWidgetItem)
from PyQt5.Qsci import *
from core.editor import Editor
from core.lexerEditor import LexerTiny
from PyQt5.QtCore import QCoreApplication, QDate, QFile, Qt, QTextStream, QSize
import sys
from core.Utils.actionTable import ActionTable
import iconos_rc
from core.Parser.tablaAnalisis import genera_tabla, tablaSL
from core.Lexer.lexer import lex
from core.Parser.parser import Evalua_cadena, Parser


class MainAppCompiB(QMainWindow):
    """Class Main"""

    def __init__(self, parent=None):
        super(MainAppCompiB, self).__init__(parent)
        self.editor = Editor()

        tiny_lexer = LexerTiny(self.editor)
        self.editor.setLexer(tiny_lexer)

        # CONFIGURACIONES INICIALES DE LA VENTANA PRINCIPAL
        self.set_init_window_ui()
        self.create_actions()
        self.set_menu()
        self.set_toolBar()
        #####
        self.create_dockTabSim()
        self.create_dockTokens()
        self.create_dockAnalisis()
        self.create_dockTabAcciones()

        #####
        self.setUnifiedTitleAndToolBarOnMac(True)

        # INICIALIZACION DEL EDITOR DE CODIGO
        self.setCentralWidget(self.editor)

    def set_init_window_ui(self):
        self.setWindowTitle('Compiladores e Interpretes B - *')
        print(self.windowTitle())
        self.resize(1000, 1000)
        self.showMaximized()

    def set_menu(self):
        menu = self.menuBar()

        # FILE MENU
        file_menu = menu.addMenu('&Archivo')
        file_menu.addAction(self.file)
        file_menu.addAction(self.open)
        file_menu.addSeparator()
        file_menu.addAction(self.save)
        file_menu.addAction(self.save_as)
        file_menu.addSeparator()
        file_menu.addAction(self.quit)

        # EDIT MENU
        edit_menu = menu.addMenu('&Editar')
        edit_menu.addAction(self.undo)
        edit_menu.addAction(self.redo)
        file_menu.addSeparator()
        edit_menu.addAction(self.copy)
        edit_menu.addAction(self.cut)
        edit_menu.addAction(self.paste)


        # CODE MENU
        code_menu = menu.addMenu('&Codigo')
        code_menu.addAction(self.compile)

        # VIEW MENU
        self.view_menu = menu.addMenu('&Ventanas')

        # VIEW HELP
        help_menu = menu.addMenu('&Ayuda')
        help_menu.addAction(self.info)

    def set_toolBar(self):
        file_toolBar = self.addToolBar('Archivo')

        file_toolBar.addAction(self.file)
        file_toolBar.addAction(self.save)

        edit_toolBar = self.addToolBar('Editar')
        edit_toolBar.addAction(self.undo)

        code_toolBar = self.addToolBar('Codigo')
        code_toolBar.addAction(self.compile)

    def create_actions(self):
        #Action file menu
        self.file = QAction(QIcon(':/iconos/documento.png'), "&Nuevo Archivo", self, shortcut=QKeySequence.New,
                            statusTip="Crea un nuevo documento", triggered=self._new_file)

        self.open = QAction(QIcon(':/iconos/abrir-archivo.png'), "&Abrir Archivo", self, shortcut=QKeySequence.Open,
                            statusTip="Abre un archivo", triggered=self._open_file)

        self.save = QAction(QIcon(':/iconos/guardar.png'), "&Guardar", self, shortcut=QKeySequence.Save,
                            statusTip="Guarda el documento actual", triggered=self._save_file)

        self.save_as = QAction(QIcon(':/iconos/guardar-como.png'), "&Guardar como...", self,
                               shortcut='Ctrl+Shift+S',
                               triggered=self._save_file_as,
                               statusTip="Guarda el codigo en un lugar especificado")

        self.quit = QAction(QIcon(':/iconos/apagar.png'), "Salir", self, shortcut=QKeySequence.Quit, statusTip="Cierra la aplicación",
                            triggered=self._quit)

        #Action Menu
        self.undo = QAction(QIcon(':/iconos/deshacer.png'), "&Deshacer", self, shortcut=QKeySequence.Undo,
                            triggered=self._undo, statusTip="Regresa un cambio")

        self.redo = QAction(QIcon(':iconos/rehacer.png'), "&Rehacer", self, shortcut=QKeySequence.Redo,
                            statusTip="Rehacer un cambio", triggered=self._redo)

        self.copy = QAction("&Copiar", self, shortcut='Ctrl+C',
                            statusTip="Copia el texto seleccionado", triggered=self._copy)

        self.cut = QAction("C&ortar", self, shortcut='Ctrl+X',
                            statusTip="Corta el texto seleccionado", triggered=self._cut)

        self.paste = QAction("&Pegar", self, shortcut='Ctrl+V',
                            statusTip="Pega el texto que se encuentra copiado", triggered=self._paste)

        #Code Menu

        self.compile = QAction(QIcon(':/iconos/compilar.png'), "Compilar", self, shortcut='F5',
                                    statusTip="Compila el codigo fuente actual", triggered=self._compile)

        self.run = QAction(QIcon(':/iconos/compilar.png'), "Compilar", self, shortcut='F5',
                                    statusTip="Compila el codigo fuente actual")

        #Help acctions
        self.info = QAction(QIcon(':/iconos/informacion.png'), "Informacion", self, shortcut='Ctrl+I',
                            triggered=self._info)

    def create_dockTabSim(self):
        dock = QDockWidget('Tabla de simbolos', self)

        self.tab_sim = QTableWidget(dock)
        dock.setWidget(self.tab_sim)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self.view_menu.addAction(dock.toggleViewAction())

    def create_dockTokens(self):
        dock = QDockWidget('Tokens', self)

        self.tab_tokens = QTableWidget(dock)
        dock.setWidget(self.tab_tokens)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self.view_menu.addAction(dock.toggleViewAction())

        ##Inicializa la tabla.
        headerLabels = ('Token', 'Valor lexico', 'tipo')
        self.tab_tokens.setColumnCount(3)
        self.tab_tokens.setHorizontalHeaderLabels(headerLabels)

    def create_dockAnalisis(self):
        dock = QDockWidget('Tabla Analisis Sintactico')

        self.tab_ans = QTableWidget(dock)
        dock.setWidget(self.tab_ans)
        dock.resize(QSize(800, 400))

        self.addDockWidget(Qt.NoDockWidgetArea, dock)
        self.view_menu.addAction(dock.toggleViewAction())

        ##Inicializa la tabla.
        headerLabels = ('Pila Acciones', 'Cadena Entrada', 'Analisis Sintactico', 'Analisis Semantico')
        self.tab_ans.setColumnCount(4)
        self.tab_ans.setHorizontalHeaderLabels(headerLabels)

        self.tab_ans.resizeColumnsToContents()

    def create_dockTabAcciones(self):
        dock = QDockWidget('Tabla de Acciones')

        self.tab_acc = QTableWidget(dock)
        dock.setWidget(self.tab_acc)
        dock.resize(QSize(800, 400))


        self.addDockWidget(Qt.NoDockWidgetArea, dock)
        self.view_menu.addAction(dock.toggleViewAction())

        table = ActionTable()
        table.load('./core/Utils/table2.csv')

        ##Inicializa tabla
        self.tab_acc.setColumnCount(table.length)
        self.tab_acc.setHorizontalHeaderLabels(table.column_names)

        ##Inserta datos
        self.tab_acc.setRowCount(len(table.elements))
        c = 0
        for n in table.elements:
            a = 0
            for p in table.column_names:
                self.tab_acc.setItem(c, a, QTableWidgetItem(n[p]))
                a = a + 1
            c = c + 1

        self.tab_acc.resizeColumnsToContents()

    def save_changes(self):
        msgBox = QMessageBox()
        msgBox.setText("Todo cambio que no haya sido guardado se perdera")
        msgBox.setInformativeText("¿Quieres guardar los cambios?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)

        res = msgBox.exec()
        if res == QMessageBox.Save:
            file = self.windowTitle().split('-')[1]
            if file == '*':
                self._save_file_as()
                self.editor.clear()
                self.setWindowTitle('Compiladores e Interpretes B - *')
            else:
                self._save_file()
                self.editor.clear()
                self.setWindowTitle('Compiladores e Interpretes B - *')
        elif res == QMessageBox.Discard:
            self.setWindowTitle('Compiladores e Interpretes B - *')
        elif res == QMessageBox.Cancel:
            return False
        return True

    ###Funciones para los eventos de las acciones###
    def _new_file(self):
        if not "*" in self.windowTitle():
            self.save_changes()

    def _open_file(self):
        """Funcion que abre un archivo de codigo fuente con extencion .tny"""
        file = QFileDialog.getOpenFileName(self, 'Abrir Codigo', '.', "Tiny (*.tny)")[0]
        if file:
            file_name = str(file).split('/')[-1]  # Para la compatibilidad en windows
            with open(file, 'rt') as text:
                if self.editor.text():
                    if self.save_changes():
                        self.editor.clear()
                        self.editor.setText(text.read())
                        self.statusBar().showMessage("Archivo '%s' cargado." % file_name, 3500)
                        self.setWindowTitle("Compiladores e Interpretes B-%s" % file)
                else:
                    self.editor.clear()
                    self.editor.setText(text.read())
                    self.statusBar().showMessage("Archivo '%s' cargado." % file_name, 3500)
                    self.setWindowTitle("Compiladores e Interpretes B-%s" % file)

    def _save_file(self):
        if not "*" in self.windowTitle():
            file = self.windowTitle().split('-')[1]
            if file:
                file_name = str(file).split('/')[-1].lstrip()#Para que funcione en windows
                with open(file, 'w') as w_file:
                    w_file.write(str(self.editor.text()))
                    self.statusBar().showMessage("Archivo '%s' guardado." % file_name, 3500)
        else:
            self._save_file_as()

    def _save_file_as(self):
        """Funcion para guardar un archivo de codigo fuente en una direcciones especificada por el usuario"""
        text = self.editor.text()
        file = QFileDialog.getSaveFileName(self, 'Guardar Codigo', '.', 'Tiny (*.tny)')[0]
        if file:
            file = file+'.tny'
            file_name = str(file).split('/')[-1] #Para que funcione en windows
            with open(file, 'w') as w_file:
                w_file.write(text)
                self.statusBar().showMessage("Archivo '%s' guardado." % file_name, 3500)
                self.setWindowTitle("Compiladores e Interpretes B-%s" % file)

    def _quit(self):
        """Funcion que termina la aplicacion"""
        self.save_changes()
        QCoreApplication.quit()

    def _undo(self):
        """Funcion accesible desde Qscintilla"""
        return self.editor.undo()

    def _redo(self):
        """Funcion accesible desde Qscintilla"""
        return self.editor.redo()

    def _copy(self):
        """Funcion accesible desde Qscintilla"""
        return  self.editor.copy()

    def _cut(self):
        """Funcion accesible desde Qscintilla"""
        return self.editor.cut()

    def _paste(self):
        """Funcion accesible desde Qscintilla"""
        return self.editor.paste()

    def _info(self):
        """Funcion del evento que invoca la informacion de la aplicacion"""
        info = '''Esta aplicacion fue escrita por Jesus Alejandro Lara para la materia de 
        Compiladores e Interpretes B'''
        QMessageBox.about(self, 'Sobre la Compiladores', info)

    def _compile(self):
        text = self.editor.text()

        tokens = lex(text)
        self.tab_tokens.setRowCount(len(tokens))
        c = 0
        for t in tokens:
            self.tab_tokens.setItem(c, 0, QTableWidgetItem(t[0]))
            self.tab_tokens.setItem(c, 1, QTableWidgetItem(t[1]))
            self.tab_tokens.setItem(c, 2, QTableWidgetItem(t[2]))
            c = c + 1
        self.tab_tokens.resizeColumnsToContents()
        cadena = ""
        for k in tokens:
            cadena = cadena + k[0]

        #parser = Evalua_cadena(cadena)
        parser = Parser()
        res = parser.evalua(tokens)

        if not res:
            QMessageBox.about(self, 'error', 'El codigo contiene errores')
        else:
            QMessageBox.about(self, 'ok', 'Codigo correcto')


        self.tab_ans.setRowCount((len(parser.tabla_ac)))

        c = 0
        for t in parser.tabla_ac:
            if t:
                self.tab_ans.setItem(c, 0, QTableWidgetItem(t[0]))
                self.tab_ans.setItem(c, 1, QTableWidgetItem(t[1]))
                self.tab_ans.setItem(c, 2, QTableWidgetItem(t[2]))
                self.tab_ans.setItem(c, 3, QTableWidgetItem('---'))
            c = c + 1
        self.tab_ans.resizeColumnsToContents()


def main():
    app = QApplication(sys.argv)
    window = MainAppCompiB()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
