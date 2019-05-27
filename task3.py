# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

list_of_first_names = []


dict_for_results = {}


for user_info in students:
    list_of_first_names.append(user_info.get('first_name'))
    for names in list_of_first_names:
        result = list_of_first_names.count(names)
        dict_for_results[names] = result
print(dict_for_results)


for name in dict_for_results:
    print(f'{name}: {dict_for_results[name]}')
    
  

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

list_of_students = []

dict_for_results = {}

for student_info in students:
    list_of_students.append(student_info.get('first_name'))
    for names in list_of_students:
        dict_for_results[names] = list_of_students.count(names)


for names_of_students in dict_for_results:
    result = max([int(dict_for_results[names_of_students]) for names_of_students in dict_for_results])
    if dict_for_results.get(names_of_students) == result:
        print(f'Самое частое имя среди учеников: {names_of_students}')


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]


x = 0

for classes in school_students:
    list_of_students = []
    dict_of_results = {}
    for student_names in classes:
        list_of_students.append(student_names.get('first_name'))
        for frequency_of_names in list_of_students:
            dict_of_results[frequency_of_names] = list_of_students.count(frequency_of_names)


    for maximum_name in dict_of_results:
        x = x + 1
        result = max(int(dict_of_results[maximum_name]) for maximum_name in dict_of_results)
        if dict_of_results.get(maximum_name) == result:
            print(f'Самое частое имя в классе {x}: {maximum_name}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


for classes in school:
    list_of_names = []
    number_of_male_gender = 0
    number_of_female_gender = 0
    for names_of_students in classes['students']:
        list_of_names.append(names_of_students.get('first_name'))


    for names in list_of_names:
        if names in is_male:
            if is_male[names] is True:
                number_of_male_gender = number_of_male_gender + 1
            else:
                number_of_female_gender = number_of_female_gender + 1

    print('В классе {} {} мальчика и {} девочки'.format(classes['class'], number_of_male_gender, number_of_female_gender))

    
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a