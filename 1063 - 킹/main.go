package main

import (
	"fmt"
)

var dir = map[string][2]int{
	"R":  {1, 0},
	"L":  {-1, 0},
	"B":  {0, -1},
	"T":  {0, 1},
	"RT": {1, 1},
	"LT": {-1, 1},
	"RB": {1, -1},
	"LB": {-1, -1},
}

func main() {
	var King, Stone string
	var N int

	fmt.Scanf("%s %s %d", &King, &Stone, &N)

	var data = make([]string, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&data[i])
	}

	var Kingx, Kingy int = int(King[0] - 'A'), int(King[1] - '1')
	var Stonex, Stoney int = int(Stone[0] - 'A'), int(Stone[1] - '1')

	for i := 0; i < N; i++ {
		//fmt.Printf("KX %d KY %d SX %d SY %d\n", Kingx, Kingy, Stonex, Stoney)

		var KingNextX, KingNextY int = Kingx + dir[data[i]][0], Kingy + dir[data[i]][1]
		var StoneNextX, StoneNextY int = Stonex, Stoney

		if KingNextX == Stonex && KingNextY == Stoney {
			StoneNextX += dir[data[i]][0]
			StoneNextY += dir[data[i]][1]
		}

		if KingNextX >= 0 && KingNextX < 8 && KingNextY >= 0 && KingNextY < 8 && StoneNextX >= 0 && StoneNextX < 8 && StoneNextY >= 0 && StoneNextY < 8 {
			Kingx, Kingy = KingNextX, KingNextY
			Stonex, Stoney = StoneNextX, StoneNextY
		}
	}

	fmt.Println(string(Kingx+'A') + string(Kingy+'1'))
	fmt.Println(string(Stonex+'A') + string(Stoney+'1'))

}
