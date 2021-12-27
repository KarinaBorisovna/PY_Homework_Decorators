from datetime import datetime

def make_log(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open ('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f'function name: {old_function.__name__}, called: {datetime.now()}, arguments: {args}, result: {result}\n')
            
        return result

    return new_function

@make_log
def make_sum(a, b):
    return a + b

@make_log
def make_dev(a, b):
    return a / b

make_sum(4, 6)
make_dev(6, 3)


def make_log_with_path(path):
    
    def _make_log(old_function):

        def new_function(*args, **kwargs):

            result = old_function(*args, **kwargs)
            with open (f'{path}\log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(f'function name: {old_function.__name__}, called: {datetime.now()}, arguments: {args}, result: {result}\n')
            
            return result

        return new_function

    return _make_log


@make_log_with_path('D:')
def make_sum(a, b):
    return a + b

make_sum(4, 6)

class FlatIterator:

    @make_log_with_path('D:')
    def __init__(self, list):
        self.list = [item for sub_list in list for item in sub_list]

    @make_log_with_path('D:')
    def __iter__(self):
        self.cursor = -1
        return self

    @make_log_with_path('D:')
    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list):
            raise StopIteration
        return self.list[self.cursor]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
	print(item) 



flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)