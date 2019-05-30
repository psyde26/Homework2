import csv

user_info = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export_dict.csv', 'w', encoding='Windows 1251', newline = '') as info:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(info, fields, delimiter=';')
    writer.writeheader()
    for user in user_info:
        writer.writerow(user)