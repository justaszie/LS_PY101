global_list = [1, 2, 3]

def my_func():
    global_list.append('44')

my_func()
print(global_list)