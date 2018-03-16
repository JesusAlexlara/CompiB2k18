from PyQt5.QtGui import (QFont, QIcon, QKeySequence, QTextCharFormat,
                         QTextCursor, QTextTableFormat)
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDockWidget, QFileDialog,
                             QFileDialog, QListWidget, QMainWindow, QMessageBox, QTextEdit, QTableWidget,
                             QTableWidgetItem)
from PyQt5.Qsci import *
from core.editor import Editor
from core.lexerEditor import LexerTiny
from PyQt5.QtCore import QCoreApplication, QDate, QFile, Qt, QTextStream
import sys
import iconos_rc


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
        self.create_dockWindow()
        self.setUnifiedTitleAndToolBarOnMac(True)

        # INICIALIZACION DEL EDITOR DE CODIGO
        self.setCentralWidget(self.editor)

    def set_init_window_ui(self):
        self.setWindowTitle('Compiladores e Interpretes B')
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

        # CODE MENU
        code_menu = menu.addMenu('&Codigo')
        code_menu.addAction(self.compilar)

        # VIEW MENU
        self.view_menu = menu.addMenu('&Ventanas')

    def set_toolBar(self):
        file_toolBar = self.addToolBar('Archivo')

        file_toolBar.addAction(self.file)
        file_toolBar.addAction(self.save)

        edit_toolBar = self.addToolBar('Editar')
        edit_toolBar.addAction(self.undo)

        code_toolBar = self.addToolBar('Codigo')
        code_toolBar.addAction(self.compilar)

    def create_actions(self):
        self.file = QAction(QIcon(':/iconos/documento.png'), "&Nuevo", self, shortcut=QKeySequence.New,
                            statusTip="Crea un nuevo documento")

        self.save = QAction(QIcon(':/iconos/guardar.png'), "&Guardar", self, shortcut=QKeySequence.Save,
                            statusTip="Guarda el documento actual")

        self.open = QAction(QIcon(':/iconos/abrir-archivo.png'), "&Abrir", self, shortcut=QKeySequence.Open,
                            statusTip="Abre un archivo", triggered=self._open_file)

        self.undo = QAction(QIcon(':/iconos/deshacer.png'), "&Deshacer", self, shortcut=QKeySequence.Undo,
                            triggered=self._undo, statusTip="Regresa un cambio")

        self.save_as = QAction(QIcon(':/iconos/guardar-como.png'), "&Guardar como...", self,
                               shortcut='Ctrl+Shift+S',
                               triggered=self._save_file_as,
                               statusTip="Guarda el codigo en un lugar especificado")

        self.compilar = QAction(QIcon(':/iconos/ensamblar.png'), "Compilar", self, shortcut="F5",
                                statusTip="Compila el archivo actual")

        self.simulateCode = QAction(QIcon(':/iconos/simular.png'), "Simular", self, shortcut="Ctrl+F5",
                                    statusTip="Simula el documento actual")

        self.quit = QAction("Salir", self, shortcut=QKeySequence.Quit, statusTip="Cierra la aplicación",
                            triggered=self._quit)

    def create_dockWindow(self):
        dock = QDockWidget('Tabla de simbolos', self)

        self.tabsim = QTableWidget(dock)
        dock.setWidget(self.tabsim)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self.view_menu.addAction(dock.toggleViewAction())

    ###Funciones para los eventos de las acciones###

    def _open_file(self):
        """Funcion que abre un archivo de codigo fuente con extencion .tny"""
        file = QFileDialog.getOpenFileName(self, 'Abrir Codigo', '.', "Tiny (*.tny)")[0]
        if file:
            file_name = str(file).split('/')[-1]  # Para la compatibilidad en windows
            with open(file, 'rt') as text:
                if self.editor.text():
                    pass
                else:
                    self.editor.setText(text.read())
                    self.statusBar().showMessage("Archivo '%s' cargado." % file_name, 3500)

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

    def _quit(self):
        """Funcion que termina la aplicacion"""
        QCoreApplication.quit()

    def _undo(self):
        """Funcion accesible desde Qscintilla"""
        return self.editor.undo()



def main():
    app = QApplication(sys.argv)
    window = MainAppCompiB()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
