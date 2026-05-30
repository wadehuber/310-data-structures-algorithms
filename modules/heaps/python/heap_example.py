"""
Example of using a LinkedHeap.

1-1 conversion of heaps/HeapExample.java
"""

import random

from linked_heap import LinkedHeap
from student_record import StudentRecord


def main():
    t = LinkedHeap()
    s = LinkedHeap()

    for ii in range(20):
        num = int(random.random() * 100)
        t.add_element(num)

    s.add_element(StudentRecord("Harrison Ford", 3.5))
    s.add_element(StudentRecord("Mark Hamil", 3.1))
    s.add_element(StudentRecord("Carrie Fisher", 3.1))
    s.add_element(StudentRecord("Adam Driver", 3.8))
    s.add_element(StudentRecord("Daisy Ridley", 3.3))
    s.add_element(StudentRecord("John Boyega", 3.3))
    s.add_element(StudentRecord("Oscar Isaac", 3.3))
    s.add_element(StudentRecord("Lupita Nyong'o", 3.9))
    s.add_element(StudentRecord("Andy Serkis", 3.3))
    s.add_element(StudentRecord("Domhnall Gleeson", 3.4))

    print("Heap t: " + str(t))
    print("Heap s: " + str(s))

    print("\nremoveMin testing s:")
    for x in range(4):
        print(s.remove_min())

    print("\nremoveMin testing t:")
    for x in range(4):
        print(t.remove_min())


if __name__ == "__main__":
    main()
