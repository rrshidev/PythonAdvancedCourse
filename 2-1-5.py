'''Китайский гороскоп назначает животным годы в 121212-летнем цикле. Один 121212-летний цикл показан в таблице ниже. Таким образом, 201220122012 год будет очередным годом дракона.'''

animal = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
period = 12
year = int(input())
index = (year + 4) % period
if index == 12:
     index = 0

print(year)
print(animal[index])