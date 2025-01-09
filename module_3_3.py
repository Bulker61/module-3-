def  print_params(a = 1, b = 'строка', c = True):
    print(a, b ,c)

print_params()
print_params(10)
print_params(10, 'текст')
print_params(10, 'текст', bool)
print_params(c=47)
print_params(b=25)
print_params(c=[1, 2, 3])
print("__________________")
print()
values_list = [1, 'тест', True]
values_dict = {'a' : 'один', 'b' : 55, 'c' : False}
print_params(*values_list)
print_params(**values_dict)
print("__________________")
print()
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)