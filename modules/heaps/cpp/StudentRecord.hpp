// StudentRecord - a comparable element to store in a heap.
//
// 1-1 conversion of heaps/StudentRecord.java
// (compareTo on the name becomes operator< / operator== on the name).
#ifndef STUDENT_RECORD_HPP
#define STUDENT_RECORD_HPP

#include <ostream>
#include <string>

class StudentRecord
{
private:
    std::string name;
    int studentNo;
    double gpa;

    static int nextNum;  // static field shared across all instances

public:
    // A default constructor for the heap's "T temp;" temporaries.
    StudentRecord() : name(""), studentNo(0), gpa(0.0) {}

    StudentRecord(std::string name, double gpa)
    {
        this->name = name;
        this->studentNo = nextNum;
        nextNum++;
        this->gpa = gpa;
    }

    std::string getName() { return name; }

    void setName(std::string name) { this->name = name; }

    double getGpa() { return gpa; }

    void setGpa(double gpa) { this->gpa = gpa; }

    // Orders by name (Java compareTo on the name string).
    bool operator<(const StudentRecord& that) const
    {
        return name < that.name;
    }

    bool operator==(const StudentRecord& that) const
    {
        return name == that.name;
    }

    friend std::ostream& operator<<(std::ostream& os, const StudentRecord& sr)
    {
        os << "[Name=" << sr.name << ", studentNo=" << sr.studentNo
           << ", gpa=" << sr.gpa << "]";
        return os;
    }
};

int StudentRecord::nextNum = 1000;

#endif
