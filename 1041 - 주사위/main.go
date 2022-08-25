package main

import (
	"fmt"
)

//1-6, 2-5, 3-4

func main() {
	var N int
	fmt.Scan(&N)

	var data = make([]int, 6)

	for i := 0; i < 6; i++ {
		fmt.Scan(&data[i])
	}

	if N == 1 {
		var dtmax int = data[0]
		for i := 1; i < 6; i++ {
			if data[i] > dtmax {
				dtmax = data[i]
			}
		}
		var ans int = 0
		for i := 0; i < 6; i++ {
			ans += data[i]
		}
		ans -= dtmax
		fmt.Println(ans)
		return
	}

	var MinimizeData = make([]int, 3)
	MinimizeData[0] = min(data[0], data[5])
	MinimizeData[1] = min(data[1], data[4])
	MinimizeData[2] = min(data[2], data[3])

	var oneMin, twoMin, threeMin int

	oneMin = MinimizeData[0]
	for i := 1; i < 3; i++ {
		if MinimizeData[i] < oneMin {
			oneMin = MinimizeData[i]
		}
	}

	threeMin = MinimizeData[0] + MinimizeData[1] + MinimizeData[2]

	var Tmpmax int = MinimizeData[0]
	for i := 0; i < 3; i++ {
		if MinimizeData[i] > Tmpmax {
			Tmpmax = MinimizeData[i]
		}
	}

	twoMin = threeMin - Tmpmax

	//ans
	var ans int = 0

	ans += oneMin * (5*(N-2)*(N-2) + 4*(N-2))
	ans += twoMin * (8*(N-2) + 4)
	ans += threeMin * 4

	fmt.Printf("%d\n", ans)

}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
