package interact

import "github.com/lib/pq"

type Respond struct{ //server -> client
	Name string
	Time int16
	Kcal int
	Kitchen int16
	Challange int16
	Exotic bool
	Smallcost bool
	Eqip pq.BoolArray
	Parameter pq.BoolArray
	TypeDish pq.BoolArray
	Meal int16
	Components pq.Int64Array
	MassComp pq.Int64Array
}

type Request struct{ //client -> server
	MaxTime int16
	Kitchen int8
	Challange int8

	Exotic int8
	SmallCost int8

	Eqip []bool // на 1 больше, первый флаг существования
	Parameter []int8
	TypeDish []int8
	Meal int8

	Components []int
	MassComp []int
}

//давай сюда же и JSON класс