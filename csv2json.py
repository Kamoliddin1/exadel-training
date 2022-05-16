import json

csvfile = 'machine.csv'
jsonfile = 'test.json'


class MyIterator:
    def __init__(self, data, line_num):
        self.start = 0
        self._data = data.split("\n")
        self.line_num = line_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.line_num:
            data = self._data[self.start]
            self.start += 1
            return data
        raise StopIteration


class CSVReader:
    def __init__(self, file, file_name):
        self.file = file
        self.file_name = file_name
        self.line_num = sum(1 for _ in open(file_name))

    def __get_data(self):
        return self.file.read()

    def get_json(self):
        my_data = self.__get_data()
        iterated_data = MyIterator(my_data, self.line_num)
        iterable_data = iter(iterated_data)
        get_keys = next(iterable_data)
        keys = get_keys.split(',')
        result = []
        while True:
            item = {}
            try:
                row = next(iterated_data)
            except StopIteration:
                break
            values = row.split(',')
            data = list(zip(keys, values))
            for i in data:
                key = i[0]
                value = i[1]
                item[key] = value
            result.append(item)
        with open(jsonfile, 'w') as jsonFile:
            jsonFile.write(json.dumps(result, indent=4))
        return json.dumps(result, indent=4)


if __name__ == "__main__":
    with open(csvfile) as csv_file:
        my_file = CSVReader(csv_file, csvfile)
        parsed = my_file.get_json()
        print(parsed)
