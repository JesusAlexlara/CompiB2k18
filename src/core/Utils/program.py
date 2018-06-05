from ..Utils.stack import Stack


class Program:
    def __init__(self):
        self.varibles = {}

        self.comp = Stack()
        self.opsum = Stack()
        self.opmult = Stack()
        self.tipo = Stack()
        self.num = Stack()
        self.id = Stack()

        self.redux = []

        ##Variables auxiliares##
        self._tipo = None
        self._varid = Stack()
        ########################

        self.switch = {
            46:self.tipo_identificadores(),
            47:self.identificadores_id(),
            48:self.ide_id(),
            61:self.int(),
            62:self.float(),
            63:self.string(),
            64:self.vent(),
            65:self.textbox(),
            66:self.label(),
            67:self.boton(),
        }

    def estructura_def_main(self):
        pass

    def def_main(self):
        pass

    def estructura_deff(self):
        pass

    def deff(self):
        pass

    def sent_declara(self):
        while self._varid.is_empty():
            self.varibles[self._varid.pop()] = [self._tipo, None]

    def def_func(self):
        pass

    def def_id_secuencia_sent(self):
        pass

    def identificadores_id(self):
        self._varid.push(self.id.pop())

    def tipo_identificadores(self):
        self._varid.push(self.id.pop())

    def ide_id(self):
        pass

    def int(self):
        self._tipo = self.tipo.pop()

    def float(self):
        self._tipo = self.tipo.pop()

    def string(self):
        self._tipo = self.tipo.pop()

    def vent(self):
        self._tipo = self.tipo.pop()

    def textbox(self):
        self._tipo = self.tipo.pop()

    def label(self):
        self._tipo = self.tipo.pop()

    def boton(self):
        self._tipo = self.tipo.pop()


    def esquema_Traduccion(self):
        for r in self.redux:
            self.switch[r]()