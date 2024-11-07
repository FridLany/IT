immutable_var= 1, 2, 3, 4, [1, 2, 3], "two"
print(immutable_var)

#Кортеж - это невозможность изменения содержания кортежа после его создания

mutable_list = [1,2,3,4,5, [1, 2, 3], True]
mutable_list[0] = 'one'
mutable_list[1] = 2
print(mutable_list)