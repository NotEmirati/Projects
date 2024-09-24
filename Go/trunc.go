package main

import ("fmt")

// truncates the float into an integer
func main() {
  var userInput float64

  fmt.Printf("Type a number: ")
  fmt.Scan(&userInput)
  fmt.Print(Your number is: %d, int(userInput))
}
