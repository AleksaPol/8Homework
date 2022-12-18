from view import show_menu as ui
from base import read_base as read_db
from module import find_employee
from module import position_employee_selection
from module import salary_employee_selection
from base import add_employee
from base import del_employee
from base import upd_employee
from base import csv_data_export
from base import json_data_export


def controller():

    position = -1

    while position != 9:
        position = ui()
        data = read_db()
        match position:
            case 1:
                find_employee(data)
            case 2:
                position_employee_selection(data)
            case 3:
                salary_employee_selection(data)
            case 4:
                add_employee(data)
            case 5:
                del_employee(data)
            case 6:
                upd_employee(data)
            case 7:
                json_data_export(data)
            case 8:
                csv_data_export(data)
    else:
        print("Выход из программы")
