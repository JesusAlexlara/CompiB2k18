class Grammar():
    def __init__(self):
        self.productions = []

    def load(self, path):
        with open(path, 'r') as txt_grammar:
            for line in txt_grammar.readlines():
                split = line.split('->')
                production = []
                production.append(split[0].replace(' ', ''))
                split = split[1].split(' ')

                for e in split:
                    if e:
                        production.append(e.replace(' ', '').replace('\n', ''))
                self.productions.append(production)

    def str(self, index):
        str_production = ''
        try:
            for p in self.productions[index][1:]:
                str_production += ' ' + p
            format = "( {} -> {} )"
            return format.format(self.productions[index][0], str_production)
        except:
            return str_production

    def get_production_x(self, index):
        return len(self.productions[index-1][1:])


if __name__ == "__main__":
    grammar = Grammar()

    grammar.load('gramatica.txt')
    print(grammar.str(1))

    print(grammar.get_production_x(4))