from PyQt5.QtGui import (QFont, QIcon, QKeySequence, QTextCharFormat,
                         QTextCursor, QTextTableFormat)
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDockWidget, QFileDialog,
                             QFileDialog, QListWidget, QMainWindow, QMessageBox, QTextEdit, QTableWidget,
                             QTableWidgetItem)
from PyQt5.Qsci import *
from core.editor import Editor, use_indentation_markers
from PyQt5.QtCore import QCoreApplication, QDate, QFile, Qt, QTextStream
import sys
import iconos_rc

class MainAppCompiB(QMainWindow):
    """Class Main"""

    def __init__(self, parent=None):
        super(MainAppCompiB, self).__init__(parent)
        self.editor = Editor()

        #CONFIGURACIONES INICIALES DE LA VENTANA PRINCIPAL
        self.set_init_window_ui()
        self.create_actions()
        self.set_menu()
        self.set_toolBar()
        self.create_dockWindow()
        self.setUnifiedTitleAndToolBarOnMac(True)

        #INICIALIZACION DEL EDITOR DE CODIGO
        self.setCentralWidget(self.editor)


    def set_init_window_ui(self):
        self.setWindowTitle('Compiladores e Interpretes B')
        #self.resize(1000, 1000)
        self.showMaximized()

    def set_menu(self):
        menu = self.menuBar()

        #FILE MENU
        file_menu = menu.addMenu('&Archivo')
        file_menu.addAction(self.file)
        file_menu.addAction(self.open)
        file_menu.addSeparator()
        file_menu.addAction(self.save)
        file_menu.addAction(self.save_as)
        file_menu.addSeparator()
        file_menu.addAction(self.quit)

        #EDIT MENU
        edit_menu = menu.addMenu('&Editar')
        edit_menu.addAction(self.undo)

        #CODE MENU
        code_menu = menu.addMenu('&Codigo')
        code_menu.addAction(self.compilar)

        #VIEW MENU
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
                                statusTip="Abre un archivo")

        self.undo = QAction(QIcon(':/iconos/deshacer.png'), "&Deshacer", self, shortcut=QKeySequence.Undo,
                            statusTip="Regresa un cambio")

        self.save_as = QAction(QIcon(':/iconos/guardar-como.png'), "&Guardar como...", self,
                               shortcut='Ctrl+Shift+S',
                               statusTip="Guarda el documento actual en un lugar especificado")

        self.compilar = QAction(QIcon(':/iconos/ensamblar.png'), "Compilar", self, shortcut="F5",
                                    statusTip="Compila el archivo actual")

        self.simulateCode = QAction(QIcon(':/iconos/simular.png'), "Simular", self, shortcut="Ctrl+F5",
                                    statusTip="Simula el documento actual")

        self.quit = QAction("Salir", self, shortcut=QKeySequence.Quit, statusTip="Cierra la aplicación")

    def create_dockWindow(self):
        dock = QDockWidget('Tabla de simbolos', self)

        self.tabsim = QTableWidget(dock)
        dock.setWidget(self.tabsim)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self.view_menu.addAction(dock.toggleViewAction())


def main():
    app = QApplication(sys.argv)
    window = MainAppCompiB()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()