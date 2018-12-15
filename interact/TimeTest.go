package interact

import (
    "time"
    "fmt"
    "math/rand"
)

type find func(string) []Respond
type parse func(Request) string

func GenTest(n int) []Request{
	rand.Seed(time.Now().UnixNano())
	var time int16 
	var kitchen, exotic, challange, smallCost, meal int8
	var j int
	var req Request
	tests := []Request{}
	b := []bool{true,false}

	for i := 0; i < n; i++{
		time = int16(rand.Intn(121) - 1)
		kitchen = int8(rand.Intn(21) - 1)
		meal = int8(rand.Intn(3) - 1)
		challange = int8(rand.Intn(4) - 1)
		exotic = int8(rand.Intn(2) - 1)
		smallCost = int8(rand.Intn(2) - 1)

		j = rand.Intn(10) + 5
		eqip := make([]bool, j)
		for k := 0; k < j; k++ { eqip[k] = b[rand.Intn(1)] }

		j = rand.Intn(10) + 5
		typeDish := make([]int8, j)
		for k := 0; k < j; k++ { typeDish[k] = int8(rand.Intn(2) - 1) }

		j = rand.Intn(10) + 5
		parameter := make([]int8, j)
		for k := 0; k < j; k++ { parameter[k] = int8(rand.Intn(2) - 1) }

		j = rand.Intn(15) + 5
		components := make([]int,j) 
		massComp := make([]int, j)

		for k:=0;k<j;k++{
			components[k] = rand.Intn(500)
			massComp[k] = rand.Intn(490) + 10
		}

		req = Request{time,kitchen,challange,exotic,smallCost,eqip,typeDish,parameter,meal,components,massComp}
		tests = append(tests,req)
	}
	return tests
}

func TimeTest(f find, g parse, test []Request) {
	var midFindTime, midParseTime time.Duration
	midParseTime = 0
	midFindTime = 0

	n := len(test)
	for i := 0; i < n; i++ {

		start := time.Now()
		s := g(test[i])
		finish := time.Now()
		midParseTime += finish.Sub(start)


		start = time.Now()
		f(s)
		finish = time.Now()
		midFindTime += finish.Sub(start)
	}

	fmt.Printf("count tests = %d\n", n)
	fmt.Print("middle parse time: ")
	fmt.Println(time.Duration(int(midParseTime)/n))
	//fmt.Println(midParseTime)
	fmt.Print("middle find time: ")
	fmt.Println(time.Duration(int(midFindTime)/n))
	//fmt.Println(midFindTime)
	
}