# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


import os


class Employee:

    def __init__(self, info_line):
        employee_info = info_line.split()
        self.first_name = employee_info[0]
        self.last_name = employee_info[1]
        self.salary = int(employee_info[2])
        self.occupation = employee_info[3]
        self.work_hours = int(employee_info[4])

    def pay_out(self, worked_out):
        modifier = 2 if worked_out > self.work_hours else 1
        return self.salary * (1 - (1 - worked_out / self.work_hours) * modifier)


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
employee_list = []
with open(os.path.join(SCRIPT_DIR, 'data', 'workers'), 'r', encoding='utf-8') as employees:
    for row, employee in enumerate(employees):
        if row > 0 and employee.strip():
            employee_list.append(Employee(employee.strip()))

with open(os.path.join(SCRIPT_DIR, 'data', 'hours_of'), 'r', encoding='utf-8') as workedout_hours:
    for record in workedout_hours:
        for employee in employee_list:
            if employee.first_name in record and employee.last_name in record:
                hours = int(record.split()[-1])
                print('{} {} {} с зарплатой {} отработал {} ч. из {} ч. и заработал {}'.format(
                    employee.occupation,
                    employee.first_name,
                    employee.last_name,
                    employee.salary,
                    hours,
                    employee.work_hours,
                    employee.pay_out(hours)
                ))