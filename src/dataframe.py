from dataframe_helper import sort_ascend
from dataframe_helper import sort_descend
from dataframe_helper import convert_to_number

class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.column_order = column_order
    
    def to_array(self):
        array = [[] for row in self.data_dict[self.column_order[0]]]
        for column in self.column_order:
            for i in range(0, len(self.data_dict[self.column_order[0]])):
                array[i].append(self.data_dict[column][i])
        return array

    def select_columns(self, columns):
        new_columns = {}
        for column in columns:
            new_columns[column] = self.data_dict[column]
        return DataFrame(new_columns, columns)

    def select_rows(self, rows):
        selected_rows = []
        arr = self.to_array()
        for row in rows:
            selected_rows.append(arr[row])
        return DataFrame.from_array(arr, self.column_order)


    def to_json(self):
        dicts = [{} for i in range(0, len(self.data_dict) + 1)]
        for i in range(0, len(dicts)):
            for column in self.column_order:
                dicts[i][column] = self.data_dict[column][i]
        return dicts

    def order_by(self, column, ascending=True):
        unsorted = []
        for i in range(0, len(self.data_dict[column])):
            unsorted.append(self.data_dict[column][i])
        if isinstance(unsorted[0], int):
            if ascending == True:
                sort = sort_ascend(unsorted)
            elif ascending == False:
                sort = sort_descend(unsorted)
        elif isinstance(unsorted[0], str):
            print("not yet")
        arrs = [[] for i in range(0, len(self.data_dict[column]) + 1)]
        if isinstance(sort[0], int):
            for i in range(0, len(self.data_dict[column])):
                index = self.data_dict[column].index(sort[i])
                for column in self.column_order:
                    arrs[i].append(self.data_dict[column][index])
        return DataFrame.from_array(arrs, self.column_order)
        

    @classmethod
    def from_array(cls, array, column_order):
        dict = {}
        for i in range(0, len(column_order)):
            column = column_order[i]
            dict[column] = []
            for i in range(0, len(array[0])):
                dict[column].append(array[i][column_order.index(column)])
        return cls(dict, column_order=column_order)


data_dict = {
    'Pete': [1, 0, 1, 0], 
    'John': [2, 1, 0, 2], 
    'Sarah': [3, 1, 4, 0]
}
"""
a = DataFrame(data_dict, column_order=['John', 'Sarah', 'Pete'])
a.to_array()
b = a.select_columns(['Sarah', 'Pete'])
b.to_array()
c = a.select_rows([1, 3])
c.to_array()
"""
data = [['Kevin', 'Fray', 5],
       ['Charles', 'Trapp', 17],
       ['Anna', 'Smith', 13],
       ['Sylvia', 'Mendez', 9]
]
d = DataFrame.from_array(data, column_order=["firstname", "lastname", "age"])
#print(d.to_json())
e = d.order_by("age", ascending=False)
