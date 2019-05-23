package main

import ("C"
"fmt")

//export Sum
func Sum(a, b int) *[]int {
    fmt.Println(a, b)
    return &[]int{a, b}
}

func main() {}