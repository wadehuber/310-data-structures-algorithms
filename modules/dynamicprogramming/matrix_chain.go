// Matrix Chain Multiplication  (CSC310 Module 11 - Dynamic Programming)
// =====================================================================
//
// m[i][j] = fewest scalar multiplications to compute A_i..A_j
// s[i][j] = split point k (the choice table) used to print the parenthesization.
//
// Run:  go run matrix_chain.go
//
// Time: Theta(n^3)   Space: Theta(n^2)
package main

import (
	"fmt"
	"math"
)

// dims has length n+1: matrix A_i is dims[i-1] x dims[i].
func matrixChainOrder(dims []int) ([][]int, [][]int) {
	n := len(dims) - 1
	m := make([][]int, n+1)
	s := make([][]int, n+1)
	for i := range m {
		m[i] = make([]int, n+1)
		s[i] = make([]int, n+1)
	}
	for length := 2; length <= n; length++ { // chain length
		for i := 1; i <= n-length+1; i++ {
			j := i + length - 1
			m[i][j] = math.MaxInt32
			for k := i; k < j; k++ { // try every split
				cost := m[i][k] + m[k+1][j] + dims[i-1]*dims[k]*dims[j]
				if cost < m[i][j] {
					m[i][j] = cost
					s[i][j] = k
				}
			}
		}
	}
	return m, s
}

func parenthesize(s [][]int, i, j int) string {
	if i == j {
		return fmt.Sprintf("A%d", i)
	}
	k := s[i][j]
	return "(" + parenthesize(s, i, k) + parenthesize(s, k+1, j) + ")"
}

func main() {
	dims := []int{30, 35, 15, 5, 10, 20, 25} // 6 matrices: A1..A6
	n := len(dims) - 1
	m, s := matrixChainOrder(dims)

	fmt.Println("Dimensions:", dims)
	fmt.Printf("Minimum scalar multiplications: %d\n", m[1][n])
	fmt.Printf("Optimal parenthesization      : %s\n", parenthesize(s, 1, n))
}
