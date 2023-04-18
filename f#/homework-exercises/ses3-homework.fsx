// ex 2.4 

let rec pclFold f init list =
    match list with
    | [] -> init
    | hd::tl -> pclFold f ( f init hd) tl

let summation f init num = f init num

let pclSum ls = pclFold (+) 0 ls

// ex 2.5

let rec pclFoldBack f ls init =
    match ls with
    | [] -> init
    | x::xs -> f x (pclFoldBack f xs init )

let pclSumWithFoldBack ls = pclFoldBack (+) ls 0

// ex 2.6

let rec pclIncList lst = 
    match lst with
    | [] -> []
    | hd::tl -> hd + 1 :: pclIncList tl

// ex 2.7

let rec pclMap func lst = 
    match lst with
    | [] -> []
    | hd::tl -> func hd :: pclMap func tl

// test pclMap (fun x -> x * 2) [ 1 .. 3];;

// ex 2.7 b
let pclIncListWithMap lst =
    let inc x = x + 1
    pclMap inc lst

// ex 2.8

let rec pclFilter lst pred =
    match lst with
    | [] -> []
    | hd::tl -> if pred hd then hd :: pclFilter tl pred
                 else pclFilter tl pred

let pclEven x = if x % 2 = 0 then true
                 else false

// ex 3.1

let countNumOfVowels (input:string) =
    let vowels = ['a'; 'e'; 'i'; 'o'; 'u']
    let vowelCount = List.fold (fun acc char -> if List.contains char vowels then acc + 1 else acc) 0 (Seq.toList input)
    let aCount = List.fold (fun acc char -> if char = 'a' then acc + 1 else acc) 0 (Seq.toList input)
    let eCount = List.fold (fun acc char -> if char = 'e' then acc + 1 else acc) 0 (Seq.toList input)
    let iCount = List.fold (fun acc char -> if char = 'i' then acc + 1 else acc) 0 (Seq.toList input)
    let oCount = List.fold (fun acc char -> if char = 'o' then acc + 1 else acc) 0 (Seq.toList input)
    let uCount = List.fold (fun acc char -> if char = 'u' then acc + 1 else acc) 0 (Seq.toList input)
    (vowelCount, aCount, eCount, iCount, oCount, uCount)

// ex 3.2

let primesUpTo n =
    let isPrime x =
        if x <= 1 then false
        else
            let maxDiv = int (sqrt (float x))
            not <| List.exists (fun i -> x % i = 0) [2 .. maxDiv]
    [2 .. n] |> List.filter isPrime

// ex 3.3
let pclFib n =
    let rec fib a b i =
        if i = n then b
        else fib b (a + b) (i + 1)
    if n <= 0 then invalidArg "n" "n must be a positive integer"
    elif n = 1 then 0
    else fib 0 1 2

// ex 3.4

let doubleNum x = x * 2
let sqrNum x = x * x

let pclQuad x = doubleNum (doubleNum x)
let pclFourth x = sqrNum (sqrNum x)