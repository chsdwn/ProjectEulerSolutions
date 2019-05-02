package main

import "fmt"

func main() {
	calculatePythagoreanTriplet(1000)
}

func calculatePythagoreanTriplet(number int) {
	remainderToBAndC := 0
	a, b, c := 0, 0, 1
	result := 0

	for a = number / 2; a > number/4; a-- {
		remainderToBAndC = number - a
		c = 1

		// Needs to check the reminder number is ever or odd
		for b = remainderToBAndC - c; b > (remainderToBAndC / 2); b-- {
			if (b*b)+(c*c) == a*a {
				result = b * c * a
				fmt.Println(c, "^ 2 + ", b, "^ 2 = ", a, "^ 2", "=> a.b.c = ", result)
				return
			}
			c += 1
		}
	}
}
