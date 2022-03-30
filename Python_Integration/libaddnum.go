//libaddnum.go
package main

import (
	"C"
	"log"
)

//export add
func add(var1, var2 int) int {
	log.Println("Given var1 --> ", var1)
	log.Println("Given var2 --> ", var2)
	return var1 + var2
}

func main() {
}

// ##### Note : #####
// https://pkg.go.dev/cmd/cgo
// This allows and makes GO codes & function as C compatible langugage
// In python we can load & run "c" libraries & functions
// Function names & Go file name should be proper in comments, to get go function exposed to python

// ##### Exporting Go Function #####
// (base) rocks-Air:Python_Integration rock$ go build -buildmode=c-shared -o libaddnum.so libaddnum.go
