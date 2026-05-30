// Example of using a LinkedHeap.
//
// 1-1 conversion of heaps/HeapExample.java
//
// Build & run:  g++ -std=c++17 HeapExample.cpp -o HeapExample && ./HeapExample
#include <cstdlib>
#include <iostream>

#include "LinkedHeap.hpp"
#include "StudentRecord.hpp"

int main()
{
    LinkedHeap<int> t;
    LinkedHeap<StudentRecord> s;

    for (int ii = 0; ii < 20; ii++)
    {
        int num = (int)((rand() / (double)RAND_MAX) * 100);
        t.addElement(num);
    }

    s.addElement(StudentRecord("Harrison Ford", 3.5));
    s.addElement(StudentRecord("Mark Hamil", 3.1));
    s.addElement(StudentRecord("Carrie Fisher", 3.1));
    s.addElement(StudentRecord("Adam Driver", 3.8));
    s.addElement(StudentRecord("Daisy Ridley", 3.3));
    s.addElement(StudentRecord("John Boyega", 3.3));
    s.addElement(StudentRecord("Oscar Isaac", 3.3));
    s.addElement(StudentRecord("Lupita Nyong'o", 3.9));
    s.addElement(StudentRecord("Andy Serkis", 3.3));
    s.addElement(StudentRecord("Domhnall Gleeson", 3.4));

    std::cout << "Heap t: " << t.toString() << std::endl;
    std::cout << "Heap s: " << s.toString() << std::endl;

    std::cout << "\nremoveMin testing s:" << std::endl;
    for (int x = 0; x < 4; x++)
        std::cout << s.removeMin() << std::endl;

    std::cout << "\nremoveMin testing t:" << std::endl;
    for (int x = 0; x < 4; x++)
        std::cout << t.removeMin() << std::endl;

    return 0;
}
