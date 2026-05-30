"""
StudentRecord - a comparable element to store in a heap.

1-1 conversion of heaps/StudentRecord.java
(compareTo on the name becomes __lt__ / __eq__ on the name).
"""


class StudentRecord:

    next_num = 1000  # static field shared across all instances

    def __init__(self, name, gpa):
        self.name = name
        self.student_no = StudentRecord.next_num
        StudentRecord.next_num += 1
        self.gpa = gpa

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

    def __str__(self):
        return "[Name=" + self.name + ", studentNo=" + str(self.student_no) + ", gpa=" + str(self.gpa) + "]"

    def __lt__(self, that):
        # Orders by name (Java compareTo on the name string).
        return self.name < that.name

    def __eq__(self, that):
        return self.name == that.name
