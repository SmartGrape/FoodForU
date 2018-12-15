package main

import (
	"net"
	"github.com/mgutz/logxi/v1"
	"os"
	//"github.com/deckarep/golang-set"
	"strconv"
	"time"	
)	

const (
	conn_host = ""
	conn_port = "8080"
	conn_type = "tcp"
)

var count = 0
//clients := mapset.NewSet()

func main() {
	l, err := net.Listen(conn_type,conn_host + ":"+ conn_port)
	if err != nil{
		log.Info("Err Listening: ", err.Error())
		os.Exit(1)
	}
	defer l.Close()

	log.Info("Linstening on "+ conn_host + ":" + conn_port)

	for {
		conn, err := l.Accept()
		if err != nil {
			log.Info("Error accepting", err.Error())
			os.Exit(1)
		}

		go handleRequest(conn)
	}
} 

func handleRequest(conn net.Conn) {
	tC := count 
	count++

	log.Info("Сlient №" + strconv.Itoa(tC) + " connected")
	mess := make([]byte, 1024)
	conn.Read(mess)
	message := string(mess)
	time.Sleep(2 * time.Second)
	log.Info("Clinent №" + strconv.Itoa(tC) + " seid "+ message)

	respond := generateRequest(message)
	log.Debug("You sent '"+ respond + "' to clients №"+strconv.Itoa(tC))
	conn.Write([]byte(respond))

	conn.Close()
}

func generateRequest(message string) string {
	return "lol"
}