class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = 0
        self.current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list >= len(self.list_of_list):
            raise StopIteration
        
        item = self.list_of_list[self.current_list][self.current_item]
        self.current_item += 1
        
        if self.current_item >= len(self.list_of_list[self.current_list]):
            self.current_item = 0
            self.current_list += 1
            
        return item

def flat_list(lst):
    return list(FlatIterator(lst))

if __name__ == '__main__':
    nested_list = [['a', 'b'], ['c', 'd'], ['e']]
    flat_result = list(FlatIterator(nested_list))
    print(f"Результат: {flat_result}")  # ['a', 'b', 'c', 'd', 'e']
    
    print(f"flat_list: {flat_list([['x'], ['y']])}")  # ['x', 'y']