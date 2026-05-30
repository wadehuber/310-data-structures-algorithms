// Tests a priority queue.
//
// 1-1 conversion of priorityqueue/PQTester.java
//
// Build & run:  g++ -std=c++17 PQTester.cpp -o PQTester && ./PQTester
#include <iostream>
#include <string>

#include "PriorityQueue.hpp"

int main()
{
    PriorityQueue<std::string> pq;

    pq.addElement("first", 1);
    pq.addElement("bbb", 200);
    pq.addElement("third", 50);
    pq.addElement("fifth", 92);
    pq.addElement("second", 10);
    pq.addElement("fourth", 55);
    pq.addElement("aaa", 200);
    pq.addElement("this one should be first", 0);

    while (!pq.isEmpty())
        std::cout << pq.removeNext() << std::endl;

    return 0;
}
