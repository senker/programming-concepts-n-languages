let rec pclFold f init lst =
    match lst with
    | [] -> init
    | h::tl -> pclFold f (f init h) tl

// higher order functions
// exercise 2.7 pclMap

let rec pclMap f = function
    | [] -> []
    | hd::tl -> f hd :: pclMap f tl

// 2.6 pclIncList
let rec pclIncList lst = 
    match lst with
    | [] -> []
    | hd::tl -> hd + 1 :: pclIncList tl // hd::tl (have something in the list) -> head + 1 :: recurse the function to the tail until empty

// increasing the list with the use of pclMap function
let incList2 lst = let inc n = n + 1 in pclMap inc lst

// exercise 2.8 pclFilter
// Filter is HOF over Lists
// remove all elements from a list
// that do not satisfy a given predicate
let rec pclFilter predicate lst = 
    match lst with 
    | [] -> []
    | x::xs -> if predicate x then x :: pclFilter predicate xs
                else pclFilter predicate xs

// Use guard to redefine filtering
let rec pclFilter2 predicate lst = 
    match lst with 
    | []                    -> []
    | x::xs when predicate x -> x :: pclFilter2 predicate xs
    | x::xs                 -> pclFilter2 predicate xs 


let pclEven n =
    if n % 2 = 0 then true
    else false

pclFilter pclEven [1 .. 10]

let rec pclSum lst = 
    match lst with
    | [] -> 0
    | hlst::tlst -> hlst + pclSum tlst

let pclSumWithFold lst = pclFold (+) 0 lst

let rec pclFoldBack f lst init =
    match lst with
    | [] -> init
    | x::xs -> f x (pclFoldBack f xs init)

//lamda function
List.map (fun x -> x + 1) [0 .. 4];;

let positiveIntegers xs =
    let isPos x = x > 0
    in List.map isPos xs

List.map((+) "Software Engineer ") ["Vladimir"; "Vova"; "Vavan"]