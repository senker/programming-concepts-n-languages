
// ex 2.1a
let vowelToUpper s  =
    match s with
    | 'a' -> "A" + s.ToString().Substring(1)
    | 'e' -> "E" + s.ToString().Substring(1)
    | 'i' -> "I" + s.ToString().Substring(1)
    | 'o' -> "O" + s.ToString().Substring(1)
    | 'u' -> "U" + s.ToString().Substring(1)
    | _ -> s.ToString()
// ex 2.1b
let rec vowelToUpperString s = 
    match s with
    | "" -> ""
    | s -> vowelToUpper s.[0] + vowelToUpperString s.[1..]
// s.[1..] is responsible for selecting the second element and onward from the provided string, in such a way
// we get rid of the first string element by converting it and afterwards pass the following elements

// ex 2.2

let rec pmLength ls =
    match ls with
    | [] -> 0
    | x::xs -> 1 + pmLength xs

let rec pclSum ls =
    match ls with
    | [] -> 0
    | x::xs -> x + pclSum xs
// ex 2.3
let rec takeSome n ls =
    match ls with
    | [] -> []
    | x::xs -> if n > 0 then x::(takeSome(n-1)) xs else [] 


















(*
// ex 2.3 

let rec takeSome n lst =
    match lst with
    | [] -> []
    | x::xs -> if n > 0 then x::(takeSome (n-1) xs) else []

// ex 2.4

let rec pclFold f init lst =
    match lst with
    | [] -> init
    | h::tl -> pclFold f (f init h) tl


     *)