package main

import "C"

//export Sum
func Sum(a, b C.int) C.int {
    return a + b
}

func main() {}