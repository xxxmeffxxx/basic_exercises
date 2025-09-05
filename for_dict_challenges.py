
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from collections import Counter
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
names = [student['first_name'] for student in students]
print(names)
students_uniq = Counter(names)
print(students_uniq)
for name, count in students_uniq.items():
    print(f"{name}: {count}")
print()

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = [student['first_name'] for student in students]
students_uniq = Counter(names)
most_name = students_uniq.most_common(1)[0][0]
print(most_name)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for ind, group in enumerate(school_students):
    names = [student['first_name'] for student in group]
    students_uniq = Counter(names)
    most_name = students_uniq.most_common(1)[0][0]
    print(f"Самое частое имя в классе {ind+1}: {most_name}")
print()
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_group in school:
    group = class_group['students']
    b = 0
    g = 0
    for student in group:
        if is_male[student['first_name']] == True:
            b += 1
        else:
            g += 1
    print(f"класс {class_group['class']}: девочки {g}, мальчики {b} ")
print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

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

for class_info in school:
    students = class_info['students']
    class_name = class_info['class']

    b = sum(1 for student in students if is_male[student['first_name']] is True)
    g = sum(1 for student in students if is_male[student['first_name']] is False)

    class_info['girls'] = g
    class_info['boys'] = b

max_g_dict = max(school, key=lambda item: item["girls"])
print(f"Больше всего девочек в классе {max_g_dict["class"]}")

max_b_dict = max(school, key=lambda item: item["boys"])
print(f"Больше всего мальчиков в классе {max_b_dict["class"]}")
