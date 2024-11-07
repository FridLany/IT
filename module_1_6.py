my_dict = {'Denis': 2001, 'Max': 2000, 'Sergey': 2005}
print('Словарь', my_dict)
print('Год рождения дениса', my_dict["Denis"])
print('Год рождения Елены', my_dict.get('Elena', 'Нету такого ключа'))
my_dict.update({'Роберт': 2002, 'Егор': 1998})
removed_year = my_dict.pop('Роберт')
print('Значение удаленного элемента \ Роберта\':', removed_year)
print('Измененный словарь', my_dict)

print()


my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list'}
print('Множество', my_set)
my_set.add('string')
my_set.add('float')
print(my_set)
my_set.discard(2)
print('Измененное множество', my_set)