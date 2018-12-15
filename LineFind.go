package main

import (
    "database/sql"
    "fmt"
    //"github.com/lib/pq"
    "bytes"
    "./interact"
    "strconv"
)

func lineFind(s string) []interact.Respond{
	//fmt.Println("reqest = " + s)
	connStr := "user=tester password=hardpass dbname=postgres"
	db, err := sql.Open("postgres", connStr)
	if err != nil{
		fmt.Println(err)
	} else {
		rows, err := db.Query(s);
		if err != nil {
			fmt.Println(err)
		}
		defer db.Close()
		defer rows.Close()

		respond := []interact.Respond{}
		for rows.Next() {
			p := interact.Respond{}
    		err := rows.Scan(&p.Name, &p.Time, &p.Kcal, &p.Kitchen, &p.Challange, &p.Exotic, &p.Smallcost, &p.Eqip, &p.Parameter, &p.TypeDish, &p.Meal, &p.Components, &p.MassComp)
    		if err != nil{
    			fmt.Println(err)
    		} else {
    			respond = append(respond, p)
    		}
		}
		return respond
	}
	return nil
}


func lineParse(req interact.Request) string{

	var l int
	var buf bytes.Buffer

	if req.MaxTime != -1 {
		buf.WriteString("time <= ")
		buf.WriteString(strconv.Itoa(int(req.MaxTime)))
	}

	if req.Kitchen != -1{
		if buf.Len() != 0 {buf.WriteString(" and ")}
		buf.WriteString("kitchen = ")
		buf.WriteString(strconv.Itoa(int(req.Kitchen)))
	}

	if req.Challange != -1{
		if buf.Len() != 0 {buf.WriteString(" and ")}
		buf.WriteString("challange = ")
		buf.WriteString(strconv.Itoa(int(req.Challange)))
	}

	switch req.SmallCost {
	case 1:
		if buf.Len() != 0 {buf.WriteString(" and ")}
		buf.WriteString("smallCost")
	case 0:
		if buf.Len() != 0 {buf.WriteString(" and ")}
		buf.WriteString("not smallCost")
	}

	switch req.Exotic {
	case 1:
		if buf.Len() != 0 {buf.WriteString(" and ")}
		buf.WriteString("exotic")
	case 0:
		if buf.Len() != 0 {buf.WriteString(" and ")}
		buf.WriteString("not exotic")
	}

	if req.Meal != -1{
		if buf.Len() != 0 {buf.WriteString(" and ")}
		buf.WriteString("(meal >> ")
		buf.WriteString(strconv.Itoa(int(req.Meal)))
		buf.WriteString(" & 1) = 1")
	}

	if req.Eqip[0] {
		l = len(req.Eqip)
		for i := 1; i < l; i++{
			if !req.Eqip[i]{
				if buf.Len() != 0 {buf.WriteString(" and ")}
				buf.WriteString("not eqip[")
				buf.WriteString(strconv.Itoa(i-1))
				buf.WriteString("]")
			}
		}
	}

	l = len(req.TypeDish)
	for i := 0; i < l; i++{
		switch req.TypeDish[i] {
		case 1:
			if buf.Len() != 0 {buf.WriteString(" and ")}
			buf.WriteString("typeDish[")
			buf.WriteString(strconv.Itoa(i))
			buf.WriteString("]")
		case 0:
			if buf.Len() != 0 {buf.WriteString(" and ")}
			buf.WriteString("not typeDish[")
			buf.WriteString(strconv.Itoa(i))
			buf.WriteString("]")
		}
	}

	l = len(req.Parameter)
	for i := 0; i < l; i++{
		switch req.Parameter[i] {
		case 1:
			if buf.Len() != 0 {buf.WriteString(" and ")}
			buf.WriteString("Parameter[")
			buf.WriteString(strconv.Itoa(i))
			buf.WriteString("]")
		case 0:
			if buf.Len() != 0 {buf.WriteString(" and ")}
			buf.WriteString("not Parameter[")
			buf.WriteString(strconv.Itoa(i))
			buf.WriteString("]")
		}
	}

	if buf.Len() != 0 { return "select * from testbd where " + buf.String() + ";" }
	return "select * from testbd;"
}

func main(){
	fmt.Println("start")
	
	//t := interact.GenTest(5)
	//for i:=0; i< len(t); i++ {fmt.Println(lineParse1(t[i]))}

	interact.TimeTest(lineFind,lineParse,interact.GenTest(100))

	
	
}

