def print_employee(employee):
    print('\nID: ', employee["id"], ' \nФамилия: ', employee["last_name"], ' \nИмя: ', employee["first_name"],
          ' \nтелефон: ', employee['phone'], ' \nДолжность:', employee['position'], ' \nЗарплата:',
          employee['salary'])


def find_employee(data):
    search_value = input("Введите данные для поиска: Id, Имя или Фамилия: ")
    flag = 0
    for employee in data:
        if search_value == employee["id"] or search_value == employee["first_name"] or search_value == employee["last_name"]:
            print_employee(employee)
            flag = 1
            break
    if flag == 0:
        print('\nтакого сотрудника нет')


def position_employee_selection(data):
    positions = []
    for employee in data:
        if not (employee['position'] in positions):
            positions.append(employee['position'])
    positions = list(enumerate(positions, 1))
    print(*positions, sep='\n')
    pos_select = int(
        input(f'\n выберите должность, введите число от 1 до {len(positions)}: '))
    for employee in data:
        if employee['position'] == positions[pos_select-1][1]:
            print_employee(employee)


def salary_employee_selection(data):
    min_salary = float(
        input("Введите нижнюю границу искомой заработной платы: "))
    max_salary = float(
        input("Введите верхнюю границу искомой заработной платы: "))
    for employee in data:
        if min_salary <= float(employee['salary']) <= max_salary:
            print_employee(employee)
