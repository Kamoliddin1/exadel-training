import re
from csv2json import MyIterator
from collections import OrderedDict

csvfile = 'test.csv'
jsonfile = 'sample.json'


class DefaultListOrderedDict(OrderedDict):
    def __missing__(self, k):
        self[k] = []
        return self[k]


class JSONReader:
    def __init__(self, file, file_name):
        self.file = file
        self.file_name = file_name
        self.line_num = sum(1 for _ in open(self.file_name))

    def __get_data(self):
        return self.file.read()

    def get_csv(self):
        my_data = self.__get_data()
        iterated_data = MyIterator(my_data, self.line_num)
        iterable_data = iter(iterated_data)
        json_datas = DefaultListOrderedDict()
        while True:
            try:
                row = next(iterable_data)
            except StopIteration:
                break
            row = row.strip()
            if row != '{' and row != '}' and row != '},' and row != '[' and row != ']':
                data = row.strip().split(':')
                # for i in range(len(data)):
                key = re.sub(',|"', '', data[0])
                value = re.sub(',|"', '', data[1])
                json_datas[key].append(value)
        return json_datas

    def write_to_csv(self):
        json_datas = self.get_csv()
        keys = json_datas.keys()
        values = json_datas.values()
        keys = ','.join(keys) + '\n'
        with open(csvfile, 'w') as csvFile:
            csvFile.write(keys)
        for i in range(len(list(values)[0])):
            lined_vals = []
            for j, _ in enumerate(values):
                lined_vals.append(list(values)[j][i])
            l = ','.join(lined_vals) + '\n'
            with open(csvfile, 'a') as csvFile:
                csvFile.write(l)


if __name__ == "__main__":
    with open(jsonfile) as json_file:
        my_file = JSONReader(json_file, jsonfile)
        print(my_file.write_to_csv())
        # parsed = my_file.get_csv()
        # print(parsed)
