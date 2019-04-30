package main

import (
	"fmt"
)

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
