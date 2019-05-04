/*
** Problem 7:
**	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
**	What is the 10 001st prime number?
 */

package main

import (
	"fmt"
)

func main() {
	calculate10001stPrimeNumber()
}

func calculate10001stPrimeNumber() {
	a := [10001]int{2}
	count := 0
	i := 3
	for {
		if a[count] != 0 {
			for j := 0; j <= count; j++ {
				if i%a[j] == 0 {
					i += 2
					break
				} else if j == count {
					count += 1
					a[count] = i
				}
			}
		}

		if count == len(a)-1 {
			break
		}
	}

	fmt.Println("10001th prime number is", a[len(a)-1])
}

func findPrime(order int) int {
	count := 1
	i := 3
	for {
		if isPrime(i) {
			count += 1
			if count == order {
				return i
			}
		}
		i += 2
	}
}

func isPrime(number int) bool {
	if number%2 != 0 {
		number += 1
	}

	for i := 1; i <= (number / 2); i += 2 {
		if i != 1 {
			if number%i == 0 {
				return false
			}
		}
	}
	return true
}
