// Exception types used by the heap classes.
//
// 1-1 conversion of the Java classes in heaps/linkedheap/exceptions/.
#ifndef EXCEPTIONS_HPP
#define EXCEPTIONS_HPP

#include <stdexcept>
#include <string>

// Represents the situation in which a collection is empty.
class EmptyCollectionException : public std::runtime_error
{
public:
    EmptyCollectionException(const std::string& collection)
        : std::runtime_error("The " + collection + " is empty.") {}
};

// Represents the situation in which a target element is not found.
class ElementNotFoundException : public std::runtime_error
{
public:
    ElementNotFoundException(const std::string& collection)
        : std::runtime_error("The target is not in the " + collection + ".") {}
};

#endif
