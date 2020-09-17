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


class School:
    """
    Объект, представляющий школу, организующую учебные классы,
    принимающую и выпускающую учеников, нанимающую педагогов
    """
    def __init__(self, grade, name):
        self.grade = grade
        self.name = name
        self._students = set()
        self._study_classes = set()
        self._teachers = set()

    def __str__(self):
        return '{} {}'.format(self.name, self.grade)

    def accept_student(self, student):
        if isinstance(student, Student):
            if not student in self._students:
                self._students.add(student)
            else:
                print('Ученик {} уже зачислен в школу'.format(student))

    def release_student(self, student, reason):
        if student in self._students:
            self._students.remove(student)
            print('{} больше не является учеником школы - {}'.format(student, reason))
        elif isinstance(student, Student):
            print('Ученик {} не числится в школе'.format(student))

    def add_study_class(self, study_class):
        if isinstance(study_class, StudyClass):
            if not study_class in self._study_classes:
                self._study_classes.add(study_class)
            else:
                print('Учебный класс {} уже организован'.format(study_class))

    def dismiss_study_class(self, study_class):
        if study_class in self._study_classes:
            self._study_classes.remove(study_class)
            print('Учебный класс {} расформирован'.format(study_class))
        elif isinstance(study_class, StudyClass):
            print('Учебный класс {} отсутствует в школе или уже расформирован'.format(study_class))

    def hire_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            if not teacher in self._teachers:
                self._teachers.add(teacher)
            else:
                print('{} уже нанят школой'.format(teacher.full_info()))

    def fire_teacher(self, teacher, reason):
        if teacher in self._teachers:
            self._teachers.remove(teacher)
            print('{} уволен из школы {}'.format(teacher.full_info(), reason))
        elif isinstance(teacher, Teacher):
            print('Чтобы уволить кого-нибудь ненужного, надо сперва нанять кого-нибудь ненужного, а у нас денег нет!')

    @property
    def student_list(self):
        return dict(('{}'.format(stdnt), stdnt,) for stdnt in self._students)

    @property
    def study_class_list(self):
        return dict(('{}'.format(stcl), stcl,) for stcl in self._study_classes)

    @property
    def teacher_list(self):
        return dict(('{}'.format(tchr), tchr,) for tchr in self._teachers)


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
        return '{}{}'.format(self._number, self._letter)

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

    school = School('High school', 'Lincoln')
    school.add_study_class(StudyClass(9, 'A'))
    school.add_study_class(StudyClass(9, 'B'))

    # проверяем, что классы созданы и вывод информации работает
    print('\n{:-^70}'.format(' инфо о созданных учебных классах '))
    for study_class in school.study_class_list.values():
        print(study_class)

    # примем в школу учеников и определим в учебный класс
    school.accept_student(
        Student('Иван', 'Иванович', 'Иванов', 
            mother=Human('Алевтина', 'Сергеевна', 'Иванова'),
            father=Human('Иван', 'Каземирович', 'Иванов'),
            study_class=school.study_class_list['9A'])
    )
    school.accept_student(
        Student('Петр', 'Петрович', 'Петров',
            mother=Human('Изабелла', 'Юрьевна', 'Петрова'),
            father=Human('Петр', 'Артурович', 'Петров'),
            study_class=school.study_class_list['9A'])
    )
    school.accept_student(
        Student('Фатых', 'Наилиевич', 'Королев',
            mother=Human('Анжелика', 'Антоновна', 'Королева'),
            study_class=school.study_class_list['9B'])
    )
    school.accept_student(
        Student('Глеб', 'Егорович', 'Сироткин')
    )

    # проверим, сработало ли зачисление учеников в классы
    print('\n{:-^70}'.format(' после зачисления учеников '))
    for study_class in school.study_class_list.values():
        print(study_class.full_info())

    # проверка вывода персональных данных
    print('\n{:-^70}'.format(' персональные данные учеников '))
    for student in school.student_list.values():
        print(student.personal_info())
    # выведем список учеников учебного класса, в котором эти ученики пока что находятся
    print('\n{:-^70}'.format(' список учеников класса '))
    print(('{}\n' * len(school.study_class_list['9A'].student_list)).format(*school.study_class_list['9A'].student_list))

    # переведём ученика в другой класс
    school.student_list['Иванов И.И.'].study_class = school.study_class_list['9B']

    # снова проверка обработки зачисления/перевода между классами
    print('{:-^70}'.format(' после перевода ученика '))
    for study_class in school.study_class_list.values():
        print(study_class.full_info())

    # проверяем, где учится каждый ученик
    print('\n{:-^70}'.format(' класс каждого ученика '))
    for student in school.student_list.values():
        print(student.study_info())

    print('\n{:-^70}'.format(' перевод ученика через списки класса '))
    # попробуем добавить в список учеников класса одного из ребят
    school.study_class_list['9A'].add_student(school.student_list['Сироткин Г.Е.'])
    # и другого; и если он уже учится в другом классе, то возникает
    # ошибочка - ученик не выписан из предыдущего класса
    school.study_class_list['9B'].add_student(school.student_list['Петров П.П.'])
    # делаем всё по правилам - выписываем из одного, вписываем в другой
    school.study_class_list['9A'].remove_student(school.student_list['Петров П.П.'])
    school.study_class_list['9B'].add_student(school.student_list['Петров П.П.'])

    # снова статистика по классам
    print('\n{:-^70}'.format(' опять после переводов учеников '))
    for study_class in school.study_class_list.values():
        print(study_class.full_info())

    # и проверка класса приписки
    print('\n{:-^70}'.format(' и снова класс каждого ученика '))
    for student in school.student_list.values():
        print(student.study_info())

    # пришло время найма преподавателей
    school.hire_teacher(
        Teacher('Сергей', 'Сергеевич', 'Сергеев', 'Математика')
    )
    school.hire_teacher(
        Teacher('Герман', 'Радиевич', 'Золото', 'Химия')
    )
    school.hire_teacher(
        Teacher('Апполинарий', 'Гераклиевич', 'Лежебоков', 'Физкультура')
    )
    school.hire_teacher(
        Teacher('Коши', 'Деламберович', 'Ландау', 'Математика')
    )

    print('\n{:-^70}'.format(' назначения преподавателей '))
    school.study_class_list['9B'].add_subject('Математика', school.teacher_list['Сергеев С.С.'])
    school.study_class_list['9B'].add_subject('Биология', school.teacher_list['Золото Г.Р.'])
    school.study_class_list['9B'].add_subject('Физкультура', school.teacher_list['Лежебоков А.Г.'])
    school.study_class_list['9B'].add_subject('Математика', school.teacher_list['Ландау К.Д.'])

    # проверим, каким же предметам обучают ученика
    print('\n{:-^70}'.format(' список предметов ученика '))
    school.student_list['Петров П.П.'].study_class.print_subject_list()

    # полный перечень преподавателей конкретного класса, хотя их там и немного
    print('\n{:-^70}'.format(' перечень преподавателей класса '))
    for teacher in school.study_class_list['9B'].subject_list.values():
        print(teacher.full_info())

    # учебный год как-будто бы прошёл, класс увеличил цифру и ждёт
    # нового расписания предметов
    print('\n{:-^70}'.format(' типа смена учебного года '))
    school.study_class_list['9B'].level_up()
    print(school.study_class_list['10B'].full_info())
    school.study_class_list['10B'].print_subject_list()

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
