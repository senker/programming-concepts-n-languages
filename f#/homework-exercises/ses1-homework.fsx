// ex 2.1
let x = 23
let myName = "Vladimir"
let age = 25
let country = "Moldova"
let y = 6 + 6

let a = 5
let b = let a = 10 in a + 5
let c = a + b

// ex 2.2

let addNum1 x = x + 1
let addNum10 x = x + 10
let addNum20 x = addNum10(addNum10 x)

// ex 2.3

let max2 x y = 
    if x > y then
        x 
    else
        y

let evenOrOdd x = 
    if x % 2 = 0 then
        printf "even number %d " x
    else
        printf "odd number %d " x

let addXY x y = 
    let z = x + y
    printf "%d will be added to %d\n" x y
    printf "%d is the result\n" z

// ex 2.4

let rec addNum_jk j k =
    match k with
    | 0 -> j
    | _ -> addNum10 (addNum_jk j (k-1))