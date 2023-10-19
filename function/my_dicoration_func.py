import sys

print(sys.path)
def my_decor(my_func):
    def make_up(var):
        my_var = my_func(var)
        return my_var.upper()
    return make_up

def my_decor_add(my_func):
    def make_add(var):
        my_var = my_func(var)
        return my_var + " Exelent!"
    return make_add


@my_decor
@my_decor_add
def my_uppper(my_text):
    return my_text

my_action_func = my_uppper("Another simple text")
print(my_action_func)

# Распоковка аргументов
def rasp(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

trek = (1, 4, 5)
trek01 = {'y': 0, 'z': 1, 'x': 1}
rasp(*trek)
rasp(**trek01)


