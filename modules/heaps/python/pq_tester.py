"""
Tests a priority queue.

1-1 conversion of priorityqueue/PQTester.java
"""

from priority_queue import PriorityQueue


def main():
    pq = PriorityQueue()

    pq.add_element("first", 1)
    pq.add_element("bbb", 200)
    pq.add_element("third", 50)
    pq.add_element("fifth", 92)
    pq.add_element("second", 10)
    pq.add_element("fourth", 55)
    pq.add_element("aaa", 200)
    pq.add_element("this one should be first", 0)

    while not pq.is_empty():
        print(pq.remove_next())


if __name__ == "__main__":
    main()
