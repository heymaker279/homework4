from application.Generator import flat_generator
from application.Iterator import FlatIterator

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for item in flat_generator(nested_list):
    print(item)

nested_list = [item for item in flat_generator(nested_list)]

for item in FlatIterator(nested_list):
    print(item)

print([item for item in FlatIterator(nested_list)])
