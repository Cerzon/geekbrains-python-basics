# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class Human:
    """
    Общий класс человеков
    """
    def __init__(self, first_name, second_name, last_name):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name

    def __str__(self):
        return '{} {}.{}.'.format(self.last_name, self.first_name[0], self.second_name[0])

    def full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.second_name)


class StudyClass:
    """
    Учебный класс
    """
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
            if subject in self._subjects:
                self.remove_subject(subject)
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
    """
    Ученик. Обычно слишком молод для создания семьи, поэтому не может быть родителем.
    """
    def __init__(self, first_name, second_name, last_name, mother=None, father=None, study_class=None):
        super().__init__(first_name, second_name, last_name)
        if isinstance(mother, Human) and not isinstance(mother, Student):
            self._mother = mother
        else:
            self._mother = None
        if isinstance(father, Human) and not isinstance(father, Student):
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
    """
    Педагог. Так же может быть родителем ученика.
    """
    def __init__(self, first_name, second_name, last_name, subject):
        super().__init__(first_name, second_name, last_name)
        self.subject = subject

    def full_info(self):
        return '{}, преподаватель предмета "{}"'.format(super().full_name(), self.subject)


if __name__ == '__main__':

    # школа может побыть и словарем со списками, этого вполне достаточно,
    # если школа всего одна
    school = {
        'study_classes': [
            StudyClass(7, 'А'),
            StudyClass(7, 'Б'),
        ],
        'students': [],
        'teachers': [],
    }

    # проверяем, что классы созданы и вывод информации работает
    print('\n{:-^70}'.format(' инфо о созданных учебных классах '))
    for study_class in school['study_classes']:
        print(study_class)

    # примем в школу учеников и определим в учебный класс
    school['students'].append(
        Student('Иван', 'Иванович', 'Иванов', 
            mother=Human('Алевтина', 'Сергеевна', 'Иванова'),
            father=Human('Иван', 'Каземирович', 'Иванов'),
            study_class=school['study_classes'][0])
    )
    school['students'].append(
        Student('Петр', 'Петрович', 'Петров',
            mother=Human('Изабелла', 'Юрьевна', 'Петрова'),
            father=Human('Петр', 'Артурович', 'Петров'),
            study_class=school['study_classes'][0])
    )
    school['students'].append(
        Student('Фатых', 'Наилиевич', 'Королев',
            mother=Human('Анжелика', 'Антоновна', 'Королева'),
            study_class=school['study_classes'][1])
    )
    school['students'].append(
        Student('Глеб', 'Егорович', 'Сироткин')
    )

    # проверим, сработало ли зачисление учеников в классы
    print('\n{:-^70}'.format(' после зачисления учеников '))
    for study_class in school['study_classes']:
        print(study_class.full_info())

    # проверка вывода персональных данных
    print('\n{:-^70}'.format(' персональные данные учеников '))
    for student in school['students']:
        print(student.personal_info())
    # выведем список учеников учебного класса, в котором эти ученики пока что находятся
    print('\n{:-^70}'.format(' список учеников класса '))
    print(('{}\n' * len(school['study_classes'][0].student_list)).format(*school['study_classes'][0].student_list))

    # переведём ученика в другой класс
    school['students'][1].study_class = school['study_classes'][1]

    # снова проверка обработки зачисления/перевода между классами
    print('{:-^70}'.format(' после перевода ученика '))
    for study_class in school['study_classes']:
        print(study_class.full_info())

    # проверяем, где учится каждый ученик
    print('\n{:-^70}'.format(' класс каждого ученика '))
    for student in school['students']:
        print(student.study_info())

    print('\n{:-^70}'.format(' перевод ученика через списки класса '))
    # попробуем добавить в список учеников класса одного из ребят
    school['study_classes'][0].add_student(school['students'][3])
    # и другого; и если он уже учится в другом классе, то возникает
    # ошибочка - ученик не выписан из предыдущего класса
    school['study_classes'][1].add_student(school['students'][0])
    # делаем всё по правилам - выписываем из одного, вписываем в другой
    school['study_classes'][0].remove_student(school['students'][0])
    school['study_classes'][1].add_student(school['students'][0])

    # снова статистика по классам
    print('\n{:-^70}'.format(' опять после переводов учеников '))
    for study_class in school['study_classes']:
        print(study_class.full_info())

    # и проверка класса приписки
    print('\n{:-^70}'.format(' и снова класс каждого ученика '))
    for student in school['students']:
        print(student.study_info())

    # пришло время найма преподавателей
    school['teachers'].append(
        Teacher('Сергей', 'Сергеевич', 'Сергеев', 'Математика')
    )
    school['teachers'].append(
        Teacher('Герман', 'Радиевич', 'Золото', 'Химия')
    )
    school['teachers'].append(
        Teacher('Апполинарий', 'Гераклиевич', 'Лежебоков', 'Физкультура')
    )
    school['teachers'].append(
        Teacher('Коши', 'Деламберович', 'Ландау', 'Математика')
    )

    print('\n{:-^70}'.format(' назначения преподавателей '))
    school['study_classes'][1].add_subject('Математика', school['teachers'][0])
    school['study_classes'][1].add_subject('Биология', school['teachers'][1])
    school['study_classes'][1].add_subject('Физкультура', school['teachers'][2])
    school['study_classes'][1].add_subject('Математика', school['teachers'][3])

    # проверим, каким же предметам обучают ученика
    print('\n{:-^70}'.format(' список предметов ученика '))
    school['students'][1].study_class.print_subject_list()

    # полный перечень преподавателей конкретного класса, хотя их там и немного
    print('\n{:-^70}'.format(' перечень преподавателей класса '))
    for teacher in school['study_classes'][1].subject_list.values():
        print(teacher.full_info())

    # учебный год как-будто бы прошёл, класс увеличил цифру и ждёт
    # нового расписания предметов
    print('\n{:-^70}'.format(' типа смена учебного года '))
    school['study_classes'][1].level_up()
    print(school['study_classes'][1].full_info())
    school['study_classes'][1].print_subject_list()

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
