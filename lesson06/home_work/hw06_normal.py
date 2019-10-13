# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class Human:
    def __init__(self, first_name, second_name, last_name):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name

    def __str__(self):
        return '{} {}.{}.'.format(self.last_name, self.first_name[0], self.second_name[0])

    def full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.second_name)


class StudyClass:

    def __init__(self, number, letter):
        self._number = number
        self._letter = letter
        self._students = set()
        self._subjects = dict()
    
    def __str__(self):
        return '{} "{}"'.format(self._number, self._letter)

    def full_info(self):
        amount_end = ''
        if len(self._students) % 10 == 0 or len(self._students) % 10 >= 5:
            amount_end = 'ов'
        elif 10 < len(self._students) < 20:
            amount_end = 'ов'
        elif 1 < len(self._students) % 10 <= 4:
            amount_end = 'а'
        return 'Класс {} "{}" - {} ученик{}'.format(
            self._number,
            self._letter,
            len(self._students),
            amount_end)

    def add_student(self, student):
        if student._study_class is None:
            self._students.add(student)
            student.study_class = self
        else:
            print('Ученик {} числится в классе {}'.format(student, student._study_class))

    def remove_student(self, student):
        if student in self._students:
            self._students.remove(student)
            del student.study_class

    @property
    def student_list(self):
        return self._students

    def add_subject(self, subject, teacher):
        if isinstance(teacher, Teacher) and subject == teacher.subject:
            self._subjects[subject] = teacher
            print('Педагог {} теперь ведёт предмет "{}" в классе {}'.format(
                teacher, subject, self
            ))
        else:
            print('При назначении педагога что-то пошло не так...')

    def remove_subject(self, subject):
        if subject in self._subjects:
            teacher = self._subjects.pop(subject)
            print('Педагог {} больше не преподаёт предмет "{}" в классе {}'.format(
                teacher, subject, self
            ))

    @property
    def subject_list(self):
        return self._subjects

    def print_subject_list(self):
        if self.subject_list:
            for subject, teacher in self.subject_list.items():
                print('{} - преподаёт {}'.format(subject, teacher))
        else:
            print('Список предметов пока пуст')
    
    def level_up(self):
        self._number += 1
        self._subjects.clear()


class Student(Human):

    def __init__(self, first_name, second_name, last_name, mother, father, study_class):
        super().__init__(first_name, second_name, last_name)
        if isinstance(mother, Human):
            self._mother = mother
        else:
            self._mother = None
        if isinstance(father, Human):
            self._father = father
        else:
            self._father = None
        self._study_class = None
        self.study_class = study_class

    def study_info(self):
        result = super().full_name()
        if not self._study_class:
            result += ', БОУК'
        else:
            result += ', ученик класса {}'.format(self._study_class)
        return result

    def personal_info(self):
        result = super().full_name()
        if self._mother:
            result += ', мать {}'.format(self._mother.full_name())
        if self._father:
            result += ', отец {}'.format(self._father.full_name())
        if not self._mother and not self._father:
            result += ', сирота'
        return result

    def set_study_class(self, study_class):
        if isinstance(study_class, StudyClass):
            if self._study_class and not study_class is self._study_class:
                self._study_class.remove_student(self)
                study_class.add_student(self)
            if self in study_class.student_list:
                self._study_class = study_class
            else:
                study_class.add_student(self)
        else:
            self._study_class = None
        
    def get_study_class(self):
        return self._study_class

    def del_study_class(self):
        self._study_class = None

    study_class = property(get_study_class, set_study_class, del_study_class, 'учебный класс')


class Teacher(Human):

    def __init__(self, first_name, second_name, last_name, subject):
        super().__init__(first_name, second_name, last_name)
        self.subject = subject

    def full_info(self):
        return '{}, преподаватель предмета "{}"'.format(super().full_name(), self.subject)


if __name__ == '__main__':

    # школа может побыть и словарем, хотя список тоже сгодился бы
    school = {
        '1A': StudyClass(1, 'А'),
        '1B': StudyClass(1, 'Б'),
    }

    # проверяем, что классы созданы и вывод информации работает
    for key, value in school.items():
        print(key, value)

    # создадим пару учеников. увы, из-за лени горе-программиста, они сироты
    # зато сразу зачислены в учебный класс
    ivanov_ii = Student('Иван', 'Иванович', 'Иванов', None, None, school['1A'])
    petrov_pp = Student('Петр', 'Петрович', 'Петров', None, None, school['1A'])

    # проверим, сработало ли зачисление учеников в классы
    for key, value in school.items():
        print(key, value.full_info())

    # убедимся, что ребята всё ещё сироты, но были бы отец и мать - тоже всё напечаталось бы
    print(ivanov_ii.personal_info())
    print(petrov_pp.personal_info())
    # выведем список учеников учебного класса, в котором эти ученики пока что находятся
    print(str('{}\n' * len(school['1A'].student_list)).format(*school['1A'].student_list))

    # переведём Петрова в другой класс
    petrov_pp.study_class = school['1B']

    # снова проверка обработки зачисления/перевода между классами
    for key, value in school.items():
        print(key, value.full_info())

    # проверяем, где учится каждый ученик
    print(ivanov_ii.study_info())
    print(petrov_pp.study_info())

    # попробуем добавить в список учеников класса одного из ребят,
    # и возникает ошибочка - ученик не выписан из предыдущего класса
    school['1B'].add_student(ivanov_ii)
    # делаем всё по правилам - выписываем из одного, вписываем в другой
    school['1A'].remove_student(ivanov_ii)
    school['1B'].add_student(ivanov_ii)

    # снова статистика по классам
    for key, value in school.items():
        print(key, value.full_info())

    # и проверка класса приписки
    print(ivanov_ii.study_info())
    print(petrov_pp.study_info())

    # пришло время найма преподавателей
    sergeev_ss = Teacher('Сергей', 'Сергеевич', 'Сергеев', 'Математика')
    school['1B'].add_subject('Математика', sergeev_ss)

    # проверим, каким же предметам обучают ученика Петрова
    petrov_pp.study_class.print_subject_list()

    # полный перечень преподавателей конкретного класса, хотя их там и немного
    for teacher in school['1B'].subject_list.values():
        print(teacher.full_info())

    # учебный год как-будто бы прошёл, класс увеличил цифру и...
    school['1B'].level_up()
    print(school['1B'].full_info())

    # ... в новом году ожидаем новые предметы, а пока они не назначены
    petrov_pp.study_class.print_subject_list()

    # в школу пришёл парнишка из Греции, а в какой класс его определить - не разобрались
    kpp = Student('Палейвктос', 'Панайотович', 'Калайдопола', None, None, None)

    # поэтому парень временно Без Определенного Учебного Класса
    print(kpp.study_info())

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
