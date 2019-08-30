#revist - https://www.safaribooksonline.com/videos/effective-python/9780134175249/9780134175249-EPLL_04_01?autoplay=false

class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name,):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Manas')
book.report_grade('Manas', 99)
book.report_grade('Manas', 98)
book.report_grade('Manas', 100)
print(book.average_grade('Manas'))

book = SimpleGradebook()
book.add_student('Manas')
book.report_grade('Manas', 99)
book.report_grade('Manas', 98)
book.report_grade('Manas', 100)
print(book.average_grade('Manas'))

#By Subject SimpleGradebook

class SimpleGradebookBySubject(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(score)

    def average_grade(self, name,):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)

        return total/count

book = SimpleGradebookBySubject()
book.add_student('Issac')
book.report_grade('Issac', 'Math', 90)
book.report_grade('Issac', 'Math', 85)
book.report_grade('Issac', 'Eng', 90)
book.report_grade('Issac', 'Eng', 80)
print(book.average_grade('Issac'))

##########################################
# Named Tuple

import collections
Grade = collections.namedtuple('Grade', ('name', 'age'))
grade = Grade('Manas', 32)
print(grade)
