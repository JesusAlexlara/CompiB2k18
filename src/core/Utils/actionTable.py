import csv

class ActionTable:
    def __init__(self):
        self.elements = []
        self.length = 0
        self.column_names = None

    def load(self, path):
        first = True
        with open(path, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                dict = {}
                c = 0
                if first:
                    self.column_names = row
                    self.length = len(self.column_names)
                    first = False
                else:
                    for column in row:
                        id = self.column_names[c]
                        dict.update({id: column})
                        c = c + 1
                    self.elements.append(dict)


if __name__ == "__main__":
    table = ActionTable()

    table.load('table.csv')
    print(table.elements[0]['sent-for'])
    print(table.elements[50]['sent-for'])
    print(table.elements[8]['identificadores'])