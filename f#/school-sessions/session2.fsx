printfn "Happy Valentine's Day ♥ ♥ ♥"
// Basic language Elements
// Core Types
// List comprehension

let rec factorialPM n =
        match n with
    | 0 -> 1
    | _ -> n * factorialPM(n-1)

// let f2 (x,y,z) = (1 parameter)
// let f2 x (2,5) = (2 parameters)
// let f1 x y z = (3 parameters)

// Construction
let student1 = (111401, "Vladimir")

// Triple tuple
let student2 = (111402, "Lukas", "IoT")

// Deconstruction - using fst, snd or pattern
let studentId = fst (111401, "Vladimir")
let studentName = snd (111401, "Vladimir")

let (x', y') = student1

let tupleAdd(x, y) = x + y

let vecAdd (x1, y1) (x2, y2) = (x1+x2, y1+y2) : float * float

vecAdd(13, 2)

1::2::3::[] // creates a list

//List.tail list // returns everything besides head
//List.head list // returns head

let n10 = [1..12] // creates a list from 1 to 12
let nstep = [0 .. 10 .. 50] // creates a list with distance of 10 until 50

List.length nstep // returns the length of the list

let slst = ["Pizza"; "Burger"; "Beer";]

List.sum nstep // sums the list

// let pclSum [1;2;3] = 1::(2::(3::[])) 

let x = 
    [ let negate x = -x
      for i in 1 .. 10 do
        if i % 2 = 0 then
            yield negate i
        else
            yield i] // syntax with list comprehension

let multipleOf x = [for i in 1 .. 10 do yield x * 1]
let multipleOf2 x = [for i in 1 .. 10 -> x * i]

// yield 
let yb =
    [for a in 1 .. 5 do
     match a with
        | 3 -> yield! ["P";"C";"L"]
        | _ -> yield a.ToString()]

let rec factorialFW n =
    match n with
    | 0 -> 1
    | _ -> if n > 0
            then n * factorialFW(n-1)
            else failwith "Non natural number argument"

//
let addNum10 x = x + 10
// add multiple tens
let addMul10 n = 
    let rec helper acc n = 
        if n >= 0 then 
            addNum10 0
        else
            acc + (helper (addNum10 0) (n-1))
    helper 0 n

let addNum_jk j k = j + addMul10 k

addNum_jk 3 7