from ..Utils.stack import Stack


class Program():
    def __init__(self):
        self.varibles = {}

        self.comp = Stack()
        self.opsum = Stack()
        self.opmult = Stack()
        self.tipo = Stack()
        self.num = Stack()
        self.id = Stack()

        self.redux = []


    def esquema_Traduccion(self):
        for r in self.redux:
            pass