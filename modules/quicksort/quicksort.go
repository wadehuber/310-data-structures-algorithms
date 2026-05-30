// quicksort.go
//
// A Go port of the quicksort example for our DSA class.
// Adapted from the code provided with:
//   Java Foundations (2nd & 3rd ed) by Lewis, DePasquale, & Chase
//   Algorithms (4th ed) by Sedgewick & Wayne
//
// Run:
//   go run quicksort.go

package main

import (
	"fmt"
	"math/rand"
	"strings"
)

// ---- Helper operations -------------------------------------------------
// These operations occur multiple times in our sorting routines,
//   so we pull them out into small helpers.

func swap(data []int, ii, jj int) {
	data[ii], data[jj] = data[jj], data[ii]
}

func isSorted(data []int) bool {
	for ii := 1; ii < len(data); ii++ {
		if data[ii] < data[ii-1] {
			return false
		}
	}
	return true
}

// ---- Quicksort ---------------------------------------------------------

func partition(data []int, min, max int) int {
	middle := min + ((max - min) / 2)

	// Use the middle data value as the partition element,
	//   then move it out of the way (into the min slot) for now.
	partitionElement := data[middle]
	swap(data, middle, min)

	left := min
	right := max

	for left < right {
		// search for an element that is > the partition element
		for left < right && data[left] <= partitionElement {
			left++
		}

		// search for an element that is < the partition element
		for data[right] > partitionElement {
			right--
		}

		// swap the elements
		if left < right {
			swap(data, left, right)
		}
	}

	// move the partition element into place
	swap(data, min, right)

	return right
}

func quickSort(data []int, min, max int) {
	if min < max {
		// create partitions
		indexOfPartition := partition(data, min, max)

		// sort the left partition (lower values)
		quickSort(data, min, indexOfPartition-1)

		// sort the right partition (higher values)
		quickSort(data, indexOfPartition+1, max)
	}
}

// quickSortAll is the convenience entry point that sorts the whole slice.
func quickSortAll(data []int) {
	quickSort(data, 0, len(data)-1)
}

// ---- Test harness ------------------------------------------------------

func printArray(a []int) {
	parts := make([]string, len(a))
	for ii, value := range a {
		parts[ii] = fmt.Sprintf("%d", value)
	}
	fmt.Println(strings.Join(parts, " "))
}

func main() {
	failures := 0

	for kk := 0; kk < 5; kk++ {
		a := make([]int, 100)
		for ii := range a {
			a[ii] = rand.Intn(1000)
		}

		fmt.Print("\nUnsorted: ")
		printArray(a)

		quickSortAll(a)

		fmt.Print("  Sorted: ")
		printArray(a)

		if !isSorted(a) {
			fmt.Println("Fail!")
			failures++
		}
	}

	fmt.Println()
	if failures == 0 {
		fmt.Printf("Test successful! (%d failures)\n", failures)
	} else {
		fmt.Printf("Test unsuccessful! (%d failures)\n", failures)
	}
}
