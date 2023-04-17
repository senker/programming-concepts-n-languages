// Introduction to F# programming
// ==============================

/// A function to add 2 to a number
let square x = x * x

// This function uses the square function 
// to build a more complex function
let sumSqr x y = square x + square y

// a comment
/// documentation
let n1 = 1
let n2 = 2
let addint12 = n1 + n2
let f x = 2 * x * x - 5 * x + 3
let result = f (n2 + 4)

// recursion
let rec factorial1 x = 
    if x <= 1 then 
        1
    else 
        x * factorial1 (x-1)

printfn "Factorial of %i is: %i" 5 (factorial1 5)
