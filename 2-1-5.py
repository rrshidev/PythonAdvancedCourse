animal = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
per = 12
year = int(input())
index = (year + 4) % 12
if index == 12:
     index = 0


print(year)
print(animal[index])