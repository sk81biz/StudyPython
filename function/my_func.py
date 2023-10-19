# Функция внутри функции
def get_speak_func(volume):
    def yall(text):
        return text.lower() + "...!" 
    def yell(text):
        return text.upper() + "...!!!"
    if volume > 1:
        return yall
    else:
        return yell

print(" Функция внутри функции")
print(get_speak_func(0.9))
test_y = get_speak_func(0.4)
print(test_y("My funck test"))

# Функция конфигуратор (фабрика)

def func_configure(x):
    def func_action(a):
        return a + x
    return func_action

func_3 = func_configure(3)
func_5 = func_configure(5)

print("Функция конфигуратор (фабрика)")
print(func_3(4))
print(func_5(9))


# Объект вызывается как функция

class MY_CLASS:
    def __init__(self, x):
        self.x = x
    def __call__(self, a):
        return self.x + a

my_ob3 = MY_CLASS(4)
print("ВЫзов объекта как функции с помощью метода __call__")
print(my_ob3(5))
print(my_ob3(10))

# функция callable  проверки возможности вызова другой функции/метода
print("Проверка вызова функции/метода")
print(callable(my_ob3))
print(callable('yall'))

# Лямбда функция
my_lym = lambda x, y, z: x * y - z

def my_lym_func(n):
    return lambda x, y: x + y + n
my_lym_realize_7 = my_lym_func(7)

print("Пример лямда функции")
print(my_lym(4, 5, 8))
print((lambda x, y: x * y)(5, 30)) 
print("Пример лямда логическое замыкание")
print(my_lym_realize_7(10, 10))



