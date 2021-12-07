class DataFrame:
    def __init__(self, data_dict, column_order):
        self.column_order = column_order
        self.data = data_dict

        self.array = [[] for row in self.data[self.column_order[0]]]
        for column in self.column_order:
            for i in range(0, len(self.data[self.column_order[0]])):
                self.array[i].append(self.data[column][i])
    
    def to_array(self):
        return self.array

    def select_columns(self, columns):
        new_columns = {}
        for column in columns:
            new_columns[column] = self.data[column]
        return DataFrame(new_columns, columns)

    def select_rows(self, rows):
        new_rows = []
        for column in self.column_order:
            row_to_append = []
            for row in rows:
                row_to_append.append(self.data[column][row])
            new_rows.append(row_to_append)
        return DataFrame.from_array(new_rows, self.column_order)

    def to_json(self):
        dicts = [{} for row in self.array]
        for column in self.column_order:
            for i in range(0, len(self.array)):
                dicts[i][column] = self.data[column][i]
        return dicts

    @classmethod
    def from_array(cls, array, column_order):
        data_dict = dict(zip(column_order, array))
        return cls(data_dict, column_order = column_order)

data_dict = {
    'Pete': [1, 0, 1, 0], 
    'John': [2, 1, 0, 2], 
    'Sarah': [3, 1, 4, 0]
}

a = DataFrame(data_dict, column_order=['John', 'Sarah', 'Pete'])
a.to_array()
b = a.select_columns(['Sarah', 'Pete'])
b.to_array()
c = a.select_rows([1, 3])
c.to_array()
data = [['Kevin','Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13], ['Sylvia', 'Mendez', 9]]
d = DataFrame.from_array(data, column_order = ["firstname", "lastname", "age"])
print(d.to_json())