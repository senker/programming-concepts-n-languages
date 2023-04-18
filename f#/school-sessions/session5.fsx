
let rec sumList lst =
    match lst with
        | [] -> 0
        | hd::tl -> hd + sumList(tl)
printfn "Sum: %d" (sumList [1 .. 2222])

let accFactorial x = 
    if x < 0 then failwith "Non natural number arg"
    // Keep track of both x and accumulator value (acc)
    let rec tailRecursiveFactorial x acc =
        if x <= 1 then
            acc
        else
            tailRecursiveFactorial (x-1) (acc * x)
    tailRecursiveFactorial x 1

let sumListRec lst =
    let rec loopSumRec lst acc =
        match lst with
        | hd::tl -> loopSumRec tl ( acc + hd )
        | [] -> acc
    loopSumRec lst 0

// print a list in the reverse order -- continuation function

let printReverse lst =
    let rec printListRevTR lst cont =
        match lst with
        // for an empty list, execute the continuation
        | [] -> cont()
        // for other lists, print the current node as part of the cont
        | hd :: tl -> 
            printListRevTR tl (fun () -> printf "%A " hd
                                         cont())
    printListRevTR lst (fun () -> printfn "Done!")

let allPositiveIntsSeq = 
    seq { for i in 1 .. System.Int32.MaxValue do yield i }

// below it fails due to memory
let allPositiveIntsList =
    [ for i in 1 .. System.Int32.MaxValue -> i ]

seq { for i in 1 .. 100 -> (i, i*i)}
Seq.map (fun i -> (i, i*i)) { 1.. 100 }
Seq.fold (+) 0 { 1 .. 5 }

let array2list a = [for i in 0 .. Array.length a - 1 -> a.[i]]

let comingEvents = 
    [
        ("Palmesondag", "April 2");
        ("Skartorsdag", "April 6");
        ("Langfredag", "April 7");
        ("Paskedag", "April 9");
    ]
    |> Map.ofList

comingEvents.["Langfredag"]

let findLangfredag = Map.find "Langfredag" comingEvents

let langfredagOpt = Map.tryFind "Langfredag" comingEvents
match langfredagOpt with
| Some(langfredag) -> printfn "Langfredag: %s" langfredag
| None -> printfn "Langfredag not found"