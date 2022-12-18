import csv
import json


def read_base():

    db_list = []
    with open("base.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=";")
        for row in reader:
            db_list.append(row)

    write_base(db_list)

    return db_list


def write_base(data, path="base.csv"):

    with open(path, "w", encoding='utf-8') as csvfile:
        fieldnames = ['id', 'last_name', 'first_name',
                      'phone', 'position', 'salary']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, delimiter=";", lineterminator="\n")
        writer.writeheader()
        for employee in data:
            writer.writerow({'id': employee['id'], 'last_name': employee['last_name'], 'first_name': employee['first_name'],
                            'phone': employee['phone'], 'position': employee['position'], 'salary': employee['salary']})


def add_employee(data):
    id_count = 0
    for employee in data:
        if int(employee['id']) > id_count:
            id_count = int(employee['id'])

    new_employee = {}
    new_employee['id'] = str(id_count+1)
    new_employee['last_name'] = input("Введите Фамилию сотрудника: ")
    new_employee['first_name'] = input("Введите Имя сотрудника: ")
    new_employee['phone'] = input("Введите телефон сотрудника: ")
    new_employee['position'] = input("Введите должность сотрудника: ")
    new_employee['salary'] = input("Введите зарплату сотрудника: ")

    data.append(new_employee)

    write_base(data)


def del_employee(data):
    id_del = input("Введите ID сотрудника для удаления записи: ")
    flag = 0
    for employee in data:
        if id_del == employee['id']:
            flag = 1
            data.remove(employee)
            print("сотрудник удален")
            write_base(data)
            break
    if flag == 0:
        "сотрудник с таким ID не найден"


def upd_employee(data):
    id_upd = input("Введите ID сотрудника для изменения данных: ")
    flag = 0
    for employee in data:
        if id_upd == employee['id']:
            flag = 1
            field = input(
                "Введите номер поля для изменения: 1-Фамилия, 2-Имя, 3-телефон, 4-должность, 5-зарплата: ")
            match field:
                case "1":
                    employee['last_name'] = input('Введите новую Фамилию:')
                case "2":
                    employee['first_name'] = input('Введите новое Имя: ')
                case "3":
                    employee['phone'] = input('Введите новый телефон: ')
                case "4":
                    employee['position'] = input('Введите новую должность: ')
                case "5":
                    employee['salary'] = input('Введите новую зарплату: ')
                case _:
                    print("ошибка ввода")

            write_base(data)
            print("\n данные обновлены")
            break
    if flag == 0:
        "сотрудник с таким ID не найден"


def csv_data_export(data):
    path_to_export = input(
        "Введите имя файла для экспорта данных в формате .csv: ") + '.csv'

    write_base(data, path_to_export)


def json_data_export(data):
    path_to_export = input(
        "Введите имя файла для экспорта данных в формате .json: ") + '.json'

    with open(path_to_export, 'w', encoding='utf-8') as file:
        for employee in data:
            json.dump(employee, file, ensure_ascii=False, indent=4)
