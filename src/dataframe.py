from dataframe_helper import sort_ascend
from dataframe_helper import sort_descend

class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.column_order = column_order
    
    def to_array(self):
        array = [[] for i in range(len(self.data_dict[self.column_order[0]]))]
        for values in self.column_order: 
            for i in range(len(array)):
                array[i].append(self.data_dict[values][i])
        return array 

    def select_columns(self, columns):
        new_columns = {}
        for column in columns:
            new_columns[column] = self.data_dict[column]
        return DataFrame(new_columns, columns)

    def select_rows(self, rows): 
        selected_rows = []
        array = self.to_array()
        for row in rows: 
            selected_rows.append(array[row])
        return DataFrame.from_array(selected_rows, self.column_order)

    def to_json(self):
        dicts = [{} for i in range(0, len(self.data_dict) + 1)]
        for i in range(0, len(dicts)):
            for column in self.column_order:
                dicts[i][column] = self.data_dict[column][i]
        return dicts

    def order_by(self, column, ascending=True):
        unsorted = []
        sort = []
        arrs = [[] for i in range(0, len(self.data_dict[column]))]
        copy = self.data_dict[column]

        for i in range(0, len(self.data_dict[column])):
            unsorted.append(self.data_dict[column][i])

        if isinstance(unsorted[0], int):
            if ascending == True:
                sort = sort_ascend(unsorted)
            elif ascending == False:
                sort = sort_descend(unsorted)

        elif isinstance(unsorted[0], str):
            if ascending == True:
                for i in range(0, len(unsorted)):
                    for j in range(0, len(unsorted)):
                        if unsorted[i][0] < unsorted[j][0]:
                            unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
                sort = unsorted

            if ascending == False:
                for i in range(0, len(unsorted)):
                    for j in range(0, len(unsorted)):
                        if unsorted[i][0] > unsorted[j][0]:
                            unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
                sort = unsorted

        for i in range(0, len(self.data_dict[column])):
            index = copy.index(sort[i])
            for column in self.column_order:
                arrs[i].append(self.data_dict[column][index])

        return DataFrame.from_array(arrs, self.column_order)
        

    @classmethod
    def from_array(cls, arr, column_order):
        dict = {}
        for values in column_order:
            dict[values] = []
            for j in range(len(arr)):
                dict[values].append(arr[j][column_order.index(values)])
        return cls(dict, column_order = column_order)

    @classmethod
    def from_json(cls, json, column_order):
        dict = {}
        for i in range(0, len(column_order)):
            column = column_order[i]
            dict[column] = []
            for i in range(0, len(json)):
                dict[column].append(json[i][column])
        return cls(dict, column_order=column_order)
