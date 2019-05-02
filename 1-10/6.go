/*
** Problem 6:
**	The sum of the squares of the first ten natural numbers is,
**	12 + 22 + ... + 102 = 385
**	The square of the sum of the first ten natural numbers is,
**	(1 + 2 + ... + 10)2 = 552 = 3025
**	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
**	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 */

package main

import "fmt"

func main() {
	var sumOfSquares int = calculateSumOfTheSquares(1, 100)
	var squareOfSum int = calculateTheSquareOfSum(1, 100)
	result := squareOfSum - sumOfSquares
	fmt.Println("Result:", squareOfSum, "-", sumOfSquares, "=", result)
}

func square(number int) int {
	return number * number
}

func calculateSumOfTheSquares(start, end int) int {
	sum := 0
	for i := start; i <= end; i++ {
		sum += square(i)
	}
	return sum
}

func calculateTheSquareOfSum(start, end int) int {
	sum := 0
	for i := start; i <= end; i++ {
		sum += i
	}
	sum = square(sum)
	return sum
}
