class FlatIterator:

    def __init__(self, unpacking_list, step=1):
        self.list = unpacking_list
        self.step = step
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.list):
            raise StopIteration
        self.cursor = self.list[self.index]
        self.index += self.step
        return self.cursor